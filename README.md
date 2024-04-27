# MyAdwaita-Colors

Python bash script to set an accent color (from 24 preset) to gnome-shell and gtk3-gtk4 themes ( gnome v46 only )

**Basic notes:**
- use a true-color gnome terminal (console, gnome-terminal) for best experience.
- install ADW-GTK3 theme  https://github.com/lassekongo83/adw-gtk3
- script find and replace colors in gnome-shell.css e gtk.css file
- if missing, script create gtk.css file in folder /home/users/.config/gtk-4.0 with following lines to set gtk4 accent colors
  -   `@define-color accent_color #3584e4`
  -   `@define-color accent_bg_color #478fe6`
- if gtk.css already exist with some customisation, insert these lines in the file, before start using this script 
- provided gnome-shell.css file is a modded version of vanilla gnome-shell theme: it use nord theme color schema for background and, mainly, less rounded borders and minor padding) 
- Only gnome-shell dark-theme. Sorry!
 
![MyAdwaita-Colors](https://raw.github.com/dasnoopy/MyAdwaita-Colors/main/screenshot/MyAdwaita-Colors.png)

**Some other info:**
 - the script use dbus-send command to reload shell theme "on-the-fly". This can be achivied only if gnome is in unsafe-mode.
   unsafe mode can be enabled/disabled using this extensions: https://github.com/linushdot/unsafe-mode-menu
 - if the extension is not installed or running, after any color change you have to use gnome-tweaks to reload MyAdwaita-Colors theme.


**How to use it:** 
1) git clone MyAdwaita-Colors repo: # git clone https://github.com/dasnoopy/MyAdwaita-Colors
2) create (if not exist) folder /home/user/.themes and copy MyAdwaita-Colors folder into it
3) copy default files into the just created folder 
4) may you want to activate the unsafe-mode extension 
5) run the gnome_colors.py script from folder /home/user/.themes/MyAdwaita-Colors
6) choose a color schema between 24
7) Enjoy Gnome!

**Other useful extension related to colors:**
- https://github.com/tuberry/color-picker (gnome-extension to pick color)

 **TODO:**
- read color combination from external conf file : only read (add/remove can be done manually)
- run script out of gnome-shell folder



