Use a true-color gnome terminal (console, gnome-terminal and so on...)
Only gnome-shell dark-theme. Sorry!

1) git clone MosLight themes : # git clone https://github.com/dasnoopy/moslight-themes

2) create (if not exist) folder /home/user/.themes and copy MyAdwaita-Colors folder into it
3) copy default files into the just created folder : MyAdwaita-Colors is a modded version og vanilla gnome-shell theme
4) move gtk.css file in /home/user/.config/gtk-4.0/ (or copy the content if already exist and in use)
5) from gnome-tweaks choose theme MyAdwaita-Colors
6) install and activate unsafe extensions if you want apply on-the-fly the MyAdwaita color shell theme with choosing it
   from gnome-tweaks
7) run the gnome_colors.py script from folder /home/user/.themes/MyAdwaita-Colors
8) choose a color schema between 24
9) Enjoy Gnome!

# apply new colors on the fly using dbus-send command (gnome v46  tested)
# gnome shell session must be in unsafe mode
# use  this extensions to temporary set gs in unsafe mode while using this script
#
#  https://github.com/linushdot/unsafe-mode-menu
#
