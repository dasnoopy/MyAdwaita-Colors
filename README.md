# MyAdwaita-Colors

Python bash script to set an accent color (from 24 preset) to gnome-shell and gtk3-gtk4 themes ( gnome v46 only )
- script find and replace colors in gnome-shell.css e gtk.css file

![MyAdwaita-Colors](https://raw.github.com/dasnoopy/MyAdwaita-Colors/main/screenshot/MyAdwaita-colors.png)


**Prerequisite:**
 - gnome-shell.css file is a modded version of vanilla gnome-shell theme
 - use a true-color gnome terminal (console, gnome-terminal) for best experience.
 - install ADW-GTK3 theme  https://github.com/lassekongo83/adw-gtk3
 - the script use dbus-send command to put gnome v46 if gnome is in a unsafe-mode and change on-the-fly the shell theme.
   unsafe-mode can be achivied temporary if this extensions is installed and active:
	 https://github.com/linushdot/unsafe-mode-menu
- Only gnome-shell dark-theme. Sorry!

**How to use it:** 
1) git clone MyAdwaita-Colors repo: # git clone https://github.com/dasnoopy/MyAdwaita-Colors
2) create (if not exist) folder /home/user/.themes and copy MyAdwaita-Colors folder into it
3) copy default files into the just created folder 
4) move gtk.css file in /home/user/.config/gtk-4.0/ (or copy the content if already exist and in use)
5) activate unsafe extensions if you want apply on-the-fly the MyAdwaita color shell theme with choosing it
   from gnome-tweaks (
7) run the gnome_colors.py script from folder /home/user/.themes/MyAdwaita-Colors
5) from gnome-tweaks choose theme MyAdwaita-Colors
8) choose a color schema between 24
9) Enjoy Gnome!

**Other useful extension related to colors:**
- https://github.com/tuberry/color-picker (gnome-extension to pick color)

 **TODO:**
- read color combination from external conf file : only read (add/remove can be done manually)



