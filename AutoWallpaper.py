import threading as t  # 导入 threading 模块并重命名为 t
import pystray as s  # 导入 pystray 模块并重命名为 s
from PIL import Image  # 导入 PIL 库中的 Image 模块

import ctypes  # 导入 ctypes 模块用于切换壁纸
from sys import *  # 从 sys 模块导入 argv 对象，用于获取输入
import time  # 导入 time 模块
import os  # 导入 os 模块


timecycle = []  # 重置 timecycle 列表
sub_thread_event = t.Event()  # 创建 Event 对象，用于线程间通信

# 创建退出图标时调用的函数
def quit(icon: s.Icon):
    icon.stop()
    #exit()

# 创建一个空函数
def do_nothing():
    10/10


# 设置壁纸的函数
def set_wallpaper(FilePath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, FilePath, 0)
def ReadConfig(File):
    global imgpath
    global delay
    global addhours
    global WallName
    imgpath = ''
    with open(File, 'r') as file:
        cfg = file.read().split(';\n')  # 读取配置文件内容并根据分号将其拆分为列表
        file.close()
    delay = 24 / float(cfg[0]) * 60  # 将配置文件中的时间间隔转换为浮点数
    for i in range(int(1440 / delay)):
        timecycle.append(i * delay)  # 根据配置文件中的时间间隔计算每个时间段的起始时间并添加到时间周期列表中
    if len(cfg) >= 2 and cfg[2] != '':
        addhours = int(cfg[2])
    else:
        addhours = time.localtime().tm_gmtoff / 60 / 60
    if len(cfg) >= 3 and cfg[3] != '':
        WallName = cfg[3]
    else:
        WallName = 'Unknown Theme'
    imgpath = '\\'.join(os.path.abspath(argv[0]).split('\\')[0:-1]) + '\\Wallpapers' + cfg[1]  # 根据配置文件中的路径模板生成实际的图像路径

# 帮助
if len(argv) < 2:
    print('AutoWallpaper.exe <AWC Config File Name> <UTC+(AutoWallpaper.exe utchelp)>')
    exit()
elif argv[1].lower() == 'help':
    print('AutoWallpaper.exe <AWC Config File Name> <UTC+(AutoWallpaper.exe utchelp)>')
    exit()
elif argv[1].lower() == 'utchelp':
    print('UTC Help:\n UK: 0\n USA: 5~10\n China: 8\n Japan/Korea: 9\n Australia: 10\nFor other countries, search Country+UTC in any search engine')
    exit()


ReadConfig(argv[1])
utcplus = float(argv[2])  # 获取命令行参数中的 UTC 值并转换为浮点数
menu = (s.MenuItem(text='AutoWallpaper', action=do_nothing), s.MenuItem(text=f'Current Wallpaper: {WallName}', action=do_nothing), s.MenuItem(text='Exit', action=quit),)
image = Image.open("Assets/Icon.png")  # 打开图像文件
icon = s.Icon("icon", image, "AutoWallpaperTrayIcon", menu)  # 创建系统托盘图标

# 主线程函数
def main_thread():
    num = 0
    while True:
        if sub_thread_event.is_set() == False:
            exit()
        CurrentTime = time.gmtime()[3] * 60 + time.gmtime()[4] + addhours * 60 + utcplus * 60 # 设置时间（加UTC和壁纸中）
        lasttime = CurrentTime
        for i in range(len(timecycle)):
            if timecycle[i] >= CurrentTime:
                set_wallpaper(imgpath.replace('*', str(i)))  # 根据当前时间选择对应的壁纸进行设置
                break
        while True:
            if sub_thread_event.is_set() == False:
                exit()
            if lasttime != CurrentTime:
                break

# 子线程函数
def sub_thread():
    sub_thread_event.set()  # 设置 Event 对象，表示子线程正在运行
    icon.run()  # 启动系统托盘图标
    sub_thread_event.clear()  # 清除 Event 对象，表示子线程已经结束

t.Thread(target=sub_thread, daemon=True).start()  # 创建子线程并启动线程
main_thread()  # 调用主线程函数进入 loop
