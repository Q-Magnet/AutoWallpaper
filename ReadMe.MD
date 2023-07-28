# AutoWallpaper

## Features of AutoWallpaper

AutoWallpaper is a software that automatically switches wallpapers, allowing changing wallpapers day and night.

It only requires 7MB Storage.

## Starting AutoWallpaper

1. Run CMD.EXE
2. go to the directory of AutoWallpaper
3. Run
    `AutoWallpaper.exe <.AWC Configuration File> <UTC Time Zone(Not needed)>`
    Then, AutoWallpaper is started.
4. find the "AutoWallpaperTrayIcon" in your system tray (in the taskbar), click it and it will show a menu, click "Exit"

  ## What is the UTC time zone and how to set it

UTC will be set by AutoWallpaper automatically

## Creating .AWC Files

.AWC File can be opened with Notepad or other TXT file Editor, it looks like this:

```
2;
\BigSur\Big Sur Graphic_*.jpg；
6;
Apple macOS BigSur Wallpaper
```

You might be confused, so here is its meaning

```
<How Many Pictures>;
<Where is the Pictures, Using * to Numbers> !AutoWallpaper's Path\Wallpapers\the directory
<hours add(for example: 1:Morning+Afternoon 2:Evening+Night, it would be the time sun rises)>
<Wallpaper Name>
```

