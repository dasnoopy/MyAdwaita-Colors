# MyAdwaita-Colors

Python bash script to set an accent color (from 24 preset) to gnome-shell and gtk3-gtk4 themes ( gnome v46 only )
- script find and replace colors in gnome-shell.css e gtk.css file
- script create gtk.css file,  if it's not exists (in folder /home/users/.config/gtk-4.0)
- provided gnome-shell.css file is a modded version of vanilla gnome-shell theme
 
![MyAdwaita-Colors](https://raw.github.com/dasnoopy/MyAdwaita-Colors/main/screenshot/MyAdwaita-Colors.png)

**Prerequisite:**

 - use a true-color gnome terminal (console, gnome-terminal) for best experience.
 - install ADW-GTK3 theme  https://github.com/lassekongo83/adw-gtk3
 - the script use dbus-send command to put gnome v46 in an unsafe-mode. This permit to change on-the-fly the shell theme.
   unsafe-mode can be enabled/disabled if this extensions is installed and active: https://github.com/linushdot/unsafe-mode-menu
 - if the extension is not installed or running, after any color change you have to use gnome-tweaks to select MyAdwaita-Colors theme
 - Only gnome-shell dark-theme. Sorry!

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



