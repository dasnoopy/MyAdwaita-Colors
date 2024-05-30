# MyAdwaita-Colors

- A gnome-shell theme ( **gnome v46 only** ) based on vanilla gnome-shell theme: it use nord theme colors schema for background and, mainly, less rounded borders and less padding.
- Provide also a python script to set an accent color (from 24 preset or from external palette file with a list of HEX colors) to gnome-shell and gtk3-gtk4 themes 
- It's a dark only gnome-shell theme. 

**Disclaimer:**
- The python script may not work properly on your system! (tested on archlinux system with gnome v46.1)

**Requirements:**
- python **3.11 / 3.12**
- **ADW-GTK3** theme https://github.com/lassekongo83/adw-gtk3 for a better gtk3/4 theme ;-)
- **gnome-tweaks** utility to change gnome-shell theme
- **users-theme extensions** for gnome (should be part of default gnome installation)

**Basic notes:**
- use a true-color gnome terminal (gnome-console, gnome-terminal) for best experience.
- if missing, python script create `colors.css` file in folder `/home/users/.config/gtk-4.0` with following lines to set default gnome accent colors:
  -   `@define-color accent_color #3584e4`
  -   `@define-color accent_bg_color #478fe6`

![MyAdwaita-Colors](https://raw.github.com/dasnoopy/MyAdwaita-Colors/main/screenshot/MyAdwaita-Colors.png)

**Some other info:**
 - the script use dbus-send command to reload shell theme "on-the-fly". This can be achivied only if gnome is in unsafe-mode.
   unsafe mode can be enabled/disabled using this extensions: https://github.com/linushdot/unsafe-mode-menu
 - if the extension is not installed or running, after any color change you have to use gnome-tweaks to reload MyAdwaita-Colors theme.

**How to use it:** 
1) git clone MyAdwaita-Colors repo:	`# git clone https://github.com/dasnoopy/MyAdwaita-Colors`
2) create (if not exist) folder `/home/your_account/.local/share/themes` and copy MyAdwaita-Colors folder into it
3) create or modify the file `/home/your_account/.config/gtk-4.0/gtk.css`, adding this line: 
  -   `@import 'colors.css';`
  -   it will import some colors definition from file colors.css that will be create by the script itself

3) using gnome-tweaks, choose MyAdwaita-Colors as shell and legacy applications theme...
4) run the `gnome_colors.py` script from folder `/home/user/.local/share/themes/MyAdwaita-Colors/src` (see below for a description of all script options)
5) choose a color schema between 24 preset (or load from an external file containing a list of HEX colors using  the -f option )
6) (run gnome-tweaks to reload the shell theme if unsafe-mode extension is not installed/running)
7) Enjoy new colors!

**scritp options:** 
```
usage: gnome-colors.py [-h] [-c] [-i] [-t] [-f LOAD_COLORS]

MyAdwaita-Colors: a python script to set gnome-shell v46 accent color

options:
  -h, --help            show this help message and exit
  -c, --check           check if there are duplicates HEX colors into the color list provided
  -i, --info            show list of all accent colors with extra info like RGB and HLS values
  -t, --test            show some HEX colors to test true-color terminal capability.
  -f LOAD_COLORS, --file LOAD_COLORS
                        load accent colors from an external text file that contains a list of HEX colors
```

**Other useful extension related to colors:**
- https://github.com/tuberry/color-picker (gnome-extension to pick color)

 **TODO:**



