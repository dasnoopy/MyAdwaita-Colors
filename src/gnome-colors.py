#!/usr/bin/python3
#
# @author: Andrea Antolini (https://github.com/Dasnoopy)
# @license: GNU General Public License v3.0
# @link: https://github.com/dasnoopy/MyAwaita-Colors

import os
import sys
import argparse
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

# function to convert the input and 
# check a value or value range
def checker(a):
	num = int(a)
	if num == 0 :
		raise argparse.ArgumentTypeError('Invalid value!')
	return num

# passing arguments and/or define some variabiles
# Create the parser
parser = argparse.ArgumentParser()

parser.add_argument('-c','--check-colors', action='store_true', dest='check_colors', default=False,
		help='check if there are duiplicate HEX colors in list provided')

parser.add_argument('-l','--list-colors', action='store_true', dest='list_colors', default=False,
		help='show list of colors schema, useful with -s option')

parser.add_argument('-s','--set-colors', action='store_true', dest='set_colors', default=False,
			help='set directly a new colors schema from 24 presets')

args = parser.parse_args()

checkColors = args.check_colors
listColors = args.list_colors
setColors = args.set_colors

# define global variables
curr_dir = os.getcwd()
iniFname = 'colors.ini'
gtk4Fname = os.path.expanduser('~') + "/.config/gtk-4.0/colors.css"
cssFname = os.path.expanduser('~') + "/.local/share/themes/MyAdwaita-Colors/gnome-shell/gnome-shell.css"
svgFname = os.path.expanduser('~') + "/.local/share/themes/MyAdwaita-Colors/gnome-shell/toggle-on.svg"
config = configparser.ConfigParser()


# first color is the accent color (primary)
# second color is the ligher accent color (secondary) 
# secondary color could be primary + 120B02 (hex)
# ALL 48 colors MUST be different!

colors_list = [['#c1392b','#e84c3d'],
               ['#d25400','#e45f02'],
               ['#ffcc02','#ffd709'],
               ['#a7a37e','#b9ae80'],
               ['#434c5e','#4c566a'],
               ['#30b0c7','#40c8e0'],
               ['#9b4ddf','#bf5af2'],
               ['#3b6073','#4a7586'],
               ['#3584e4','#478fe6'],
               ['#16a086','#1bbc9b'],
               ['#27ae61','#2dcc70'],
               ['#5e5c64','#706766'],
               ['#7e8c8d','#95a5a5'],
               ['#8fb021','#a5c63b'],
               ['#745dc5','#8668c7'],
               ['#63452c','#75502e'],
               ['#8d44ad','#9a59b5'],
               ['#d95459','#ef727a'],
               ['#32ade6','#64d2ff'],
               ['#d45b9e','#f47cc3'],
               ['#b25657','#c46159'],
               ['#a2845e','#ac8e68'],
               ['#5e81ac','#708cae'],
               ['#384c81','#5165a2']]

# set nr of colors combination defined in colors_list
nr_of_colors = len(colors_list)


## sorted color list
#colors_list.sort()

def check_colors():
# check for duplicates colors in colors_list
	colors_dup_list = colors_list
	for test in colors_dup_list:
		result = [(item, i) for i, lst in enumerate(colors_list) for item in test if item in lst]
		print(f"- {test}  >> {result}")



def read_all_files():
# if ini file is missing, create it with some default colors(from gnome HIG palette)
	if not os.path.exists(iniFname):
		config['COLORS'] = {'hexprimary': '#3584e4', 'hexsecondary': '#478fe6', 'rgbaprimary': 'rgba(53, 132, 228,'}
		write_file()
		
	# Read ini file...
	config.read(iniFname)
	
	global search_primary_color
	global search_secondary_color
	global search_rgba_color

	search_primary_color = config['COLORS']['hexprimary']
	search_secondary_color = config['COLORS']['hexsecondary']
	search_rgba_color = config['COLORS']['rgbaprimary'] 

def get_current_schema():
	#index of current color schema
	#if schema not found between 24 built-in presets , 0 is returned!
	global idx
	while True:
		try:
			idx=int ((next(i for i, w in enumerate(colors_list) if search_primary_color in w and search_secondary_color in w) + 1))
			break
		except StopIteration:
			idx=0
			break
		return idx

def print_matrix_with_indices(list):
	index=0
	print (f"{colors.reset}")
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
			print (f" {index + 1:02d} "'\033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm ' + (list[index][0]) + '\033[0m\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm ' + (list[index][1]) + ' \033[0m', end='')
			index += 1
		# Print a new line after each row
		print('')
	print (f"{colors.reset}")


def interactive_color_selection():

	global replace_primary_color
	global replace_secondary_color
	global replace_rgba_color

	# convert hex color to RGB just to print colors on terminal
	rgb1 = hex_to_rgb(search_primary_color)
	rgb2 = hex_to_rgb(search_secondary_color)

	R1 = str(rgb1[0])
	G1 = str(rgb1[1])
	B1 = str(rgb1[2])

	R2 = str(rgb2[0])
	G2 = str(rgb2[1])
	B2 = str(rgb2[2])

	# clean screen and welcome message
	os.system('clear')
	print (f"{colors.reset}{colors.bold}{colors.fg.lightgreen}GNOME-COLORS.PY: change accent color for MyAdwaita-Colors theme.{colors.reset}")
	print (f"{colors.reset}{colors.bold}{colors.fg.lightgrey}"'═'*84)
	print ('')
	print ('Color schema currently applied is nr. '+ f"{idx:02d} "'\033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm ' + search_primary_color  + '\033[0m' '\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm ' + search_secondary_color + ' \033[0m')
	# print color list
	print_matrix_with_indices(colors_list)
	print (f"{colors.reset}{colors.bold}{colors.fg.lightgrey}"'─'*84)
	print (f"{colors.reset}", end='')

	x = ''
	while not (x.isdigit() and int(x) in range(1, nr_of_colors + 1)):
	    x = input(f'Choose a new accent colors schema (1 to {nr_of_colors}): ')

	# set new colors
	replace_primary_color = (colors_list[int(x)-1])[0]
	replace_secondary_color  = (colors_list[int(x)-1])[1]

	# some test before save and apply new color schema 
	if replace_primary_color == '' or replace_secondary_color == '':
		 exit_on_error ('[I] no news colors defined: exit!')
	elif replace_primary_color == search_secondary_color:
		exit_on_error('[W] unable to proceed: new lighter color is equal to current darker color!')
	elif replace_secondary_color == search_primary_color:
		exit_on_error('[W] unable to proceed: new darker color is equal to current ligher color!')
	elif replace_primary_color == replace_secondary_color:
		exit_on_error('[W] unable to proceed: new lighter and darker color are the same!')
	elif replace_primary_color == search_primary_color and replace_secondary_color == search_secondary_color:
		exit_on_error('[I] nothing to change : active and choosen colors schema are equal!')

	# get new rgba color from ligher color
	replace_rgba_color = 'rgba' + str(hex_to_rgb(replace_primary_color)).rstrip(')') +','

	reply = confirm_prompt("Are you sure to continue?")
	if reply == False:
		exit_on_error('[I] exit without do any change!')

def write_all_files ():
	# Opening our text file in read only
	# mode using the open() function
	with open(cssFname, 'r', encoding='utf-8') as file:
		data = file.read()
		# Searching and replacing the text
		# using the replace() function
		data = data.replace(search_primary_color, replace_primary_color)
		data = data.replace(search_secondary_color, replace_secondary_color)
		data = data.replace(search_rgba_color, replace_rgba_color)

	# Opening our text file in write only
	# mode to write the replaced content
	with open(cssFname, 'w', encoding='utf-8') as file:
		file.write(data)

	#update also toogle-on.svg with accent color...
	with open(svgFname, 'r', encoding='utf-8') as file:
		data = file.read()
		data = data.replace(search_primary_color, replace_primary_color)
	with open(svgFname, 'w', encoding='utf-8') as file:
		file.write(data)

	# if colors.css file is missing, create and populated it...
	# make sure to add  " @import 'colors.css'; " line to gtk.css
	if not os.path.exists(gtk4Fname):
		# Open the file in append mode
		with open(gtk4Fname, 'a', encoding='utf-8') as file:
		# Append content to the file
			file.write('/* accent color */')
			file.write('\n @define-color accent_color ' + replace_primary_color + ';')
			file.write('\n @define-color accent_bg_color ' + replace_secondary_color + ';')

	# otherwise search and replace colors,  always in gtk.css
	# be sure that two lines @define-color must be exists
	with open(gtk4Fname, 'r', encoding='utf-8') as file:
		data = file.read()
		data = data.replace(search_primary_color, replace_primary_color)
		data = data.replace(search_secondary_color, replace_secondary_color)
	with open(gtk4Fname, 'w', encoding='utf-8') as file:
		file.write(data)
		

	#write INI file with new colors
	config['COLORS']['hexprimary'] = replace_primary_color
	config['COLORS']['hexsecondary'] = replace_secondary_color
	config['COLORS']['rgbaprimary'] = replace_rgba_color
	write_file()

def apply_theme():
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

# main program
def main():
	# parse arguments
	if checkColors:
		check_colors()

	elif listColors:
		print_matrix_with_indices(colors_list)
	
	elif setColors:
		sys.exit(0)

	else:
		read_all_files()
		get_current_schema()
		interactive_color_selection()
		write_all_files()
		apply_theme()
		
	# exit program
	sys.exit(0)

if __name__ == '__main__':
	main()