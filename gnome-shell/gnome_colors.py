#!/usr/bin/python3
#
# @author: Andrea Antolini (https://github.com/Dasnoopy)
# @license: GNU General Public License v3.0
# @link: https://github.com/dasnoopy/moslight-themes


# TODO List
# tema  salvabili e richiamambili in seguito 
#

import os
import sys
import configparser

class colors:
	reset = '\033[0m'
	bold = '\033[01m'
	disable = '\033[02m'
	underline = '\033[04m'
	reverse = '\033[07m'
	strikethrough = '\033[09m'
	invisible = '\033[08m'

	class fg:
		black = '\033[30m'
		red = '\033[31m'
		green = '\033[32m'
		orange = '\033[33m'
		blue = '\033[34m'
		purple = '\033[35m'
		cyan = '\033[36m'
		lightgrey = '\033[37m'
		darkgrey = '\033[90m'
		lightred = '\033[91m'
		lightgreen = '\033[92m'
		yellow = '\033[93m'
		lightblue = '\033[94m'
		pink = '\033[95m'
		lightcyan = '\033[96m'

	class bg:
		black = '\033[40m'
		red = '\033[41m'
		green = '\033[42m'
		orange = '\033[43m'
		blue = '\033[44m'
		purple = '\033[45m'
		cyan = '\033[46m'
		lightgrey = '\033[47m'

def exit_on_error(message: str):
	print('')
	print (f"{colors.reset}{colors.fg.yellow}{message}{colors.reset}")
	print('')
	sys.exit(1)

def confirm_prompt(question: str) -> bool:
    reply = None
    while reply not in ("y", "n"):
        reply = input(f"{question} (y/n): ").casefold()
    return (reply == "y")

def hex_to_rgb(hexa):
	hexa = hexa.lstrip('#')
	return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))

# Just a small function to write the ini file
def write_file():
	config.write(open(iniFname, 'w', encoding='utf-8'))

flatred         = '#d02b3b','#ba181b' #1
flatorange      = '#f59a2f','#fd7c0f' #2
flatyellow      = '#f5c211','#e5a50a' #3
flatsand        = '#a68c71','#c0833f' #4
flatnavyblue    = '#4c566a','#434c5e' #5
flatblack       = '#2f2f2f','#242424' #6
flatmagenta     = '#9a59b5','#8c43ac' #7
flatteal        = '#607d8b','#4d646f' #8
flatskyblue     = '#3584e4','#1a5fb4' #9
flatgreen       = '#2dcc70','#27ae61' #10
flatmint        = '#1bbc9b','#16a086' #11
flatwhite       = '#9a9996','#5e5c64' #12
flatgray        = '#95a5a5','#7e8c8d' #13
flatforestgreen = '#345f41','#2e5037' #14
flatpurple      = '#8560ff','#7b50ff' #15
flatbrown       = '#986a44','#63452c' #16
flatplum        = '#5e335e','#4f2b4f' #17
flatwatermelon  = '#ef727a','#d95459' #18
flatlime        = '#a2c95d','#7ebd61' #19
flatpink        = '#f47cc3','#d45b9e' #20
flatmaroon      = '#79302a','#662722' #21
flatcoffee      = '#a28671','#8e725d' #22
flatpowderblue  = '#81a1c1','#5e81ac' #23
flatblue        = '#5165a2','#384c81' #24

colors_list = [flatred,flatorange,flatyellow,flatsand,flatnavyblue,flatblack,
               flatmagenta,flatteal,flatskyblue,flatgreen,flatmint,flatwhite,
               flatgray,flatforestgreen,flatpurple,flatbrown,flatplum,flatwatermelon,
               flatlime,flatpink,flatmaroon,flatcoffee,flatpowderblue,flatblue]

# clean screen and welcome message
os.system('clear')
# define some variables
iniFname = 'colors.ini'
cssFname = os.path.expanduser('~') + "/.config/gtk-4.0/gtk.css"
config = configparser.ConfigParser()

# if ini file is missing, create it with some default colors(from gnome HIG palette)
if not os.path.exists(iniFname):
	config['COLORS'] = {'hexlighter': '#3584e4', 'hexdarker': '#478fe6', 'rgbalighter': 'rgba(53, 132, 228,'}
	write_file()
	
# Read ini file...
config.read(iniFname)
search_lighter_color = config['COLORS']['hexlighter']
search_darker_color = config['COLORS']['hexdarker']
search_rgba_color = config['COLORS']['rgbalighter'] 

rgb1 = hex_to_rgb(search_lighter_color)
rgb2 = hex_to_rgb(search_darker_color)

R1 = str(rgb1[0])
G1 = str(rgb1[1])
B1 = str(rgb1[2])

R2 = str(rgb2[0])
G2 = str(rgb2[1])
B2 = str(rgb2[2])

print (f"{colors.reset}{colors.bold}{colors.fg.lightgreen}Change accent color for gnome shell and gtk.css version 46.x{colors.reset}")
print ('')
print ('Current color schema: '' \033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm ' + search_lighter_color + ' \033[0m' '\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm ' + search_darker_color + ' \033[0m')
print ('')

def print_matrix_with_indices(list):
    index=0
    # Loop over each row
    for i in range(6):
        # Loop over each column in the current row
        for j in range(4):
            # Print element at row i, column j
            rgb1 = hex_to_rgb(list[index][0])
            rgb2 = hex_to_rgb(list[index][1])
            R1 = str(rgb1[0])
            G1 = str(rgb1[1])
            B1 = str(rgb1[2])
            R2 = str(rgb2[0])
            G2 = str(rgb2[1])
            B2 = str(rgb2[2])
            print (f" {index + 1:>2}) "'\033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm ' + (list[index][0]) + ' \033[0m' '\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm ' + (list[index][1]) + ' \033[0m', end=' ')
            index += 1
        # Print a new line after each row
        print()

# Test the function with our matrix
print_matrix_with_indices(colors_list)
print('')

x = ''
n = len(colors_list)

while not (x.isdigit() and int(x) in range(1, n + 1)):
    x = input(f'Choose a color schema? (1 to {n}): ')

replace_lighter_color = (colors_list[int(x)-1])[0]
replace_darker_color  = (colors_list[int(x)-1])[1]

# some checks
if replace_lighter_color == '' or replace_darker_color == '':
	 exit_on_error ('[Info] no news colors defined: exit!')
elif replace_lighter_color == search_darker_color:
	exit_on_error('[Warning] unable to proceed: new lighter color is equal to current darker color!')
elif replace_darker_color == search_lighter_color:
	exit_on_error('[Warning] unable to proceed: new darker color is equal to current ligher color!')
elif replace_lighter_color == replace_darker_color:
	exit_on_error('[Warning] unable to proceed: new lighter and darker color are the same!')
elif replace_lighter_color == search_lighter_color and replace_darker_color == search_darker_color:
	exit_on_error('[Info] nothing to change : current and new color schema are equal!')

# get shadow-box rgba color from ligher color
replace_rgba_color = 'rgba' + str(hex_to_rgb(replace_lighter_color)).rstrip(')') +','

reply = confirm_prompt("Are you sure to proceed?")
if reply == False:
	exit_on_error('[Info] exit without do any change!')

# Opening our text file in read only
# mode using the open() function
with open(r'gnome-shell.css', 'r', encoding='utf-8') as file:
	data = file.read()
	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_lighter_color, replace_lighter_color)
	data = data.replace(search_darker_color, replace_darker_color)
	data = data.replace(search_rgba_color, replace_rgba_color)

# Opening our text file in write only
# mode to write the replaced content
with open(r'gnome-shell.css', 'w', encoding='utf-8') as file:
	file.write(data)

#update also svg accent color (toggle-on.savg must be exist)
svg="toggle-on.svg"

with open(svg, 'r', encoding='utf-8') as file:
	data = file.read()
	data = data.replace(search_lighter_color, replace_lighter_color)
with open(svg, 'w', encoding='utf-8') as file:
	file.write(data)

# if gtk.css file is missing, create and populated it...
if not os.path.exists(cssFname):
	# Open the file in append mode
	with open(cssFname, 'a', encoding='utf-8') as file:
	# Append content to the file
		file.write('/* accent color */')
		file.write('\n @define-color accent_color ' + replace_lighter_color + ';')
		file.write('\n @define-color accent_bg_color ' + replace_darker_color + ';')

# otherwise search and replace colors,  always in gtk.css
# be sure that two lines @define-color must be exists
with open(cssFname, 'r', encoding='utf-8') as file:
	data = file.read()
	data = data.replace(search_lighter_color, replace_lighter_color)
	data = data.replace(search_darker_color, replace_darker_color)
with open(cssFname, 'w', encoding='utf-8') as file:
	file.write(data)
	

#write INI file with new colors
config['COLORS']['hexlighter'] = replace_lighter_color
config['COLORS']['hexdarker'] = replace_darker_color
config['COLORS']['rgbalighter'] = replace_rgba_color
write_file()

# apply new colors on the fly using dbus-send command (gnome v46  tested)
# gnome shell session must be in unsafe mode
# use  this extensions to temporary set gs in unsafe mode while using this script
#
#  https://github.com/linushdot/unsafe-mode-menu
#
os.system("dbus-send --session --dest=org.gnome.Shell --print-reply --type=method_call /org/gnome/Shell org.gnome.Shell.Eval string:'Main.loadTheme(); ' > /dev/null")
# final greetings
print ('')
print (f"{colors.reset}{colors.bold}{colors.fg.orange}Done. Enjoy your new gnome-shell accent color ;-){colors.reset}")
print ('')

sys.exit(0)
