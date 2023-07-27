import ctypes
from sys import argv
import time
import os


timecycle = []

def set_wallpaper(FilePath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, FilePath, 0)

if len(argv) < 2:
    print('AutoWallpaper.exe <AWC Config File Name> <UTC+(AutoWallpaper.exe utchelp)>')
    exit()
elif argv[1].lower() == 'help':
    print('AutoWallpaper.exe <AWC Config File Name> <UTC+(AutoWallpaper.exe utchelp)>')
    exit()
elif argv[1].lower() == 'utchelp':
    print('UTC Help:\n UK: 0\n USA: 5~10\n China: 8\n Japan/Korea: 9\n Australia: 10\nFor other countries, search Country+UTC in any search engine')
    exit()


utcplus = float(argv[2])


with open(argv[1], 'r') as file:
    cfg = file.read().split(';')
    file.close()
for i in range(int(1440 / int(cfg[0]))):
    timecycle.append(i * int(cfg[0]))
delay = int(cfg[0])
imgpath = '\\'.join(os.path.abspath(argv[0]).split('\\')[0:-1]) + cfg[1]


num = 0
while True:
    CurrentTime = time.gmtime()[3] * 60 + time.gmtime()[4]
    lasttime = CurrentTime
    for i in range(len(timecycle)):
        if timecycle[i] >= CurrentTime:
            set_wallpaper(imgpath.replace('*', str(i)))
            break
    while True:
        if lasttime != CurrentTime:
            break