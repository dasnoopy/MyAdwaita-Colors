# MyAdwaita-Colors

- A gnome-shell theme ( **gnome v46 only** ) based on vanilla gnome-shell theme: it use nord theme color schema for background and, mainly, less rounded borders and minor padding.
- Provide also a python script to set an accent color (from 24 preset) to gnome-shell and gtk3-gtk4 themes 
- It's a dark only gnome-shell theme. 

**Disclaimer:**
- The python script may not work properly on your system! (tested on archlinux system with gnome46.1)

**Requirements:**
- python 3.1x
- install ADW-GTK3 theme https://github.com/lassekongo83/adw-gtk3 for a better gtk3/4 theme ;-)
- install gnome-tweaks utility to change gnome-shell theme
- install and activate gnome-shell users-theme extensions (should be part of default gnome installation)

**Basic notes:**
- use a true-color gnome terminal (gnome-console, gnome-terminal) for best experience.
- script searches for and replaces colors in gnome-shell.css e gtk.css file
- if missing, script create `gtk.css` file in folder `/home/users/.config/gtk-4.0` with following lines to set default gnome accent colors
  -   `@define-color accent_color #3584e4`
  -   `@define-color accent_bg_color #478fe6`
- if gtk.css already exist with some customisation, insert, manually, these lines in the file, before start using this script 
 
![MyAdwaita-Colors](https://raw.github.com/dasnoopy/MyAdwaita-Colors/main/screenshot/MyAdwaita-Colors.png)

**Some other info:**
 - the script use dbus-send command to reload shell theme "on-the-fly". This can be achivied only if gnome is in unsafe-mode.
   unsafe mode can be enabled/disabled using this extensions: https://github.com/linushdot/unsafe-mode-menu
 - if the extension is not installed or running, after any color change you have to use gnome-tweaks to reload MyAdwaita-Colors theme.


**How to use it:** 
1) git clone MyAdwaita-Colors repo:	`# git clone https://github.com/dasnoopy/MyAdwaita-Colors`
2) create (if not exist) folder `/home/user/.local/share/themes` and copy MyAdwaita-Colors folder into it
3) using gnome-tweaks, choose MyAdwaita-Colors as shell and legacy applications theme...
4) run the `gnome_colors.py` script from folder `/home/user/.local/share/themes/MyAdwaita-Colors/src`
5) choose a color schema between 24 preset 
6) (run gnome-tweaks to reload the shell theme if unsafe-mode extension is not installed/running)
7) Enjoy new colors!

**Other useful extension related to colors:**
- https://github.com/tuberry/color-picker (gnome-extension to pick color)

 **TODO:**
- read color combination from external conf file : only read (add/remove can be done manually)
- better gtk.css management
  - add lines in append and only at first run and if file already exist



