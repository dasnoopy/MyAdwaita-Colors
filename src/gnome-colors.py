#!/usr/bin/python3
#
# @author: Andrea Antolini (https://github.com/Dasnoopy)
# @license: GNU General Public License v3.0
# @link: https://github.com/dasnoopy/MyAwaita-Colors

import os
import sys
import argparse
import configparser
import colorsys

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

# function to convert the input and 
# check a value or value range
def checker(a):
	num = int(a)
	if num == 0 or num > 24:
		raise argparse.ArgumentTypeError('Invalid value!')
	return num

# passing arguments and/or define some variabiles
# Create the parser
parser = argparse.ArgumentParser()

parser.add_argument('-c','--check-colors', action='store_true', dest='check_colors', default=False,
		help='check if there are duiplicate HEX colors in list provided')

parser.add_argument('-l','--list-colors', action='store_true', dest='list_colors', default=False,
		help='show list of colors schema')

parser.add_argument('-s','--sort-colors', action='store_true', dest='sort_colors', default=False,
		help='sort list of colors schema ordered by HEX value')

parser.add_argument('-a','--apply-colors', action='store', dest='apply_colors',type=checker,
		help='apply a colors schema from 1 to 24 directly')

args = parser.parse_args()

checkColors = args.check_colors
listColors = args.list_colors
sortColors = args.sort_colors
applyColors = args.apply_colors


# define global variables
curr_dir = os.getcwd()
iniFname = 'colors.ini'
cssFname = os.path.expanduser('~') + "/.config/gtk-4.0/colors.css"
shellFname = os.path.expanduser('~') + "/.local/share/themes/MyAdwaita-Colors/gnome-shell/gnome-shell.css"
svgFname = os.path.expanduser('~') + "/.local/share/themes/MyAdwaita-Colors/gnome-shell/toggle-on.svg"
config = configparser.ConfigParser()

# first color is the accent color (primary)
# second color is the ligher accent color (secondary) 
# secondary color could be primary + 111111 (hex)
# All colors MUST be different and in lower case!
# for better visualization keep even num of colors (eg. 12, 18, 24, 30, ....)

colors_list = [['#bf392b','#d04a3c'],
               ['#e8710f','#ec7c1d'],
               ['#d64613','#e75724'],
               ['#a7a37e','#b9ae80'],
               ['#455a64','#546e7a'],
               ['#e5a50a','#f7ae0a'],
               ['#9b4ddf','#bf5af2'],
               ['#3b6073','#4a7586'],
               ['#3584e4','#478fe6'],
               ['#60924b','#729d4b'],
               ['#2c7873','#3e8173'],
               ['#26a269','#38ad69'],
               ['#78909c','#90a4ae'],
               ['#7bb661','#86c524'],
               ['#745dc5','#8668c7'],
               ['#028fc7','#1498c7'],
               ['#555fb0','#677cc0'],
               ['#7aa5db','#8cb0db'],
               ['#1975ff','#3284ff'],
               ['#f86368','#ff8085'],
               ['#d70751','#e90751'],
               ['#a2845e','#ac8e68'],
               ['#5e81ac','#708cae'],
               ['#384c81','#4a5783']]

# set nr of colors combination defined in colors_list
# I guess that 24 preset are a good number ;-)
nr_of_colors = len(colors_list)
# colors are listed in [nr_of_rows]
nr_of_rows = 6

# Function to validate the HTML hexadecimal color code.
def isValidHexaCode(str):
	if (str[0] != '#'):
		return False
	if (not(len(str) == 4 or len(str) == 7)):
		return False
	for i in range(1, len(str)):
		if (not((str[i] >= '0' and str[i] <= '9') or (str[i] >= 'a' and str[i] <= 'f') or (str[i] >= 'A' and str[i] <= 'F'))):
			return False
	return True

def check_colors():
	# check if colors in list are valid HEX colors

	# check for duplicates colors in colors_list
	print (f"{colors.reset}{colors.bold}{colors.fg.lightblue}"'Check for duplicated colors...')
	print (f"{colors.reset}")
	indice=0
	colors_dup_list = colors_list
	for test in colors_dup_list:
		result = [(item) for i, lst in enumerate(colors_list) for item in test if item in lst]
		if colors_list[indice][0] == colors_list[indice][1]:
			print(f"{colors.reset}{colors.bold}{colors.fg.lightred}{indice:02d} - {result}")
		else:
			print(f"{colors.reset}{indice + 1:02d} - {result}")
		indice += 1
	print('')

def read_all_files():
# if ini file is missing, create it with some default colors(from gnome HIG palette)
	if not os.path.exists(iniFname):
		config['COLORS'] = {'hexprimary': '#3584e4', 'hexsecondary': '#478fe6', 'rgbaprimary': 'rgba(53, 132, 228,'}
		config.write(open(iniFname, 'w', encoding='utf-8'))
		
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
			# convert hex color to RGB just to print colors on terminal
			rgb1 = hex_to_rgb(search_primary_color)
			rgb2 = hex_to_rgb(search_secondary_color)

			R1 = str(rgb1[0])
			G1 = str(rgb1[1])
			B1 = str(rgb1[2])

			R2 = str(rgb2[0])
			G2 = str(rgb2[1])
			B2 = str(rgb2[2])

			if not applyColors:
				print (f"{colors.reset}MyAdwaita-Colors is using schema nr. {idx:02d}: "'\033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm ' + search_primary_color + ' \033[0m' '\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm ' + search_secondary_color + ' \033[0m')
				print ('')
			break
		except StopIteration:
			idx=0
			break
		return idx

def print_matrix_with_indices(lista: list, righe: int):

	# # nr. of row can't be upper of nr_of_colors
	# if righe > nr_of_colors:
	# 	righe = nr_of_colors

	print (f"{colors.reset}"'List of available schema colors:')
	print ('')
	# Loop over each row
	for row in range(righe):
		print ('┃',end='')
	# Loop over each column in the current row
		for index in range(row, nr_of_colors, righe):
			# Print elements
			rgb1 = hex_to_rgb(lista[index][0])
			rgb2 = hex_to_rgb(lista[index][1])
			R1 = str(rgb1[0])
			G1 = str(rgb1[1])
			B1 = str(rgb1[2])
			R2 = str(rgb2[0])
			G2 = str(rgb2[1])
			B2 = str(rgb2[2])
			print (f" {colors.reset}{index + 1:02d}: "'\033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm ' + (lista[index][0]) + ' \033[0m\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm ' + (lista[index][1]) + ' \033[0m', end='')
		# Print a new line after each row
		print('')
	print ('')

def interactive_color_selection():
	global replace_primary_color
	global replace_secondary_color
	global replace_rgba_color

	# clean screen and welcome message
	if not applyColors:
		x = ''
		while not (x.isdigit() and int(x) in range(1, nr_of_colors + 1)):
			x = input(f'Choose a new accent schema colors (1 to {nr_of_colors}): ')
		reply = confirm_prompt("Are you sure to continue?")
		if reply == False:
			exit_on_error('[I] exit without do any change!')
	else:
		x = applyColors
		
	# set new colors
	replace_primary_color = (colors_list[int(x) - 1])[0]
	replace_secondary_color  = (colors_list[int(x) - 1])[1]

	# some test before save and apply new color schema 
	if replace_primary_color == search_secondary_color:
		exit_on_error('[w] unable to proceed: new lighter color is equal to current darker color!')
	elif replace_secondary_color == search_primary_color:
		exit_on_error('[w] unable to proceed: new darker color is equal to current ligher color!')
	elif replace_primary_color == replace_secondary_color:
		exit_on_error('[w] unable to proceed: new lighter and darker color are equal!')
	elif replace_primary_color == search_primary_color and replace_secondary_color == search_secondary_color:
		exit_on_error('[w] nothing to change : active and choosen schema colors are equal!')

	# get new rgba color from ligher color
	replace_rgba_color = 'rgba' + str(hex_to_rgb(replace_primary_color)).rstrip(')') +','

def write_all_files ():
	# Opening our text file in read only
	# mode using the open() function
	with open(shellFname, 'r', encoding='utf-8') as file:
		data = file.read()
		# Searching and replacing the text
		# using the replace() function
		data = data.replace(search_primary_color, replace_primary_color)
		data = data.replace(search_secondary_color, replace_secondary_color)
		data = data.replace(search_rgba_color, replace_rgba_color)
	# Opening our text file in write only mode to write the replaced content
	with open(shellFname, 'w', encoding='utf-8') as file:
		file.write(data)

	#update also toogle-on.svg with accent color...
	with open(svgFname, 'r', encoding='utf-8') as file:
		data = file.read()
		data = data.replace(search_primary_color, replace_primary_color)
	with open(svgFname, 'w', encoding='utf-8') as file:
		file.write(data)

	# if colors.css file is missing, create and populated it...
	# make sure to add  " @import 'colors.css'; " line to gtk.css
	if not os.path.exists(cssFname):
		# Open the file in append mode
		with open(cssFname, 'a', encoding='utf-8') as file:
		# Append content to the file
			file.write('/* accent color */')
			file.write('\n @define-color accent_color ' + replace_primary_color + ';')
			file.write('\n @define-color accent_bg_color ' + replace_secondary_color + ';')

	# otherwise search and replace colors,  always in colors.css
	# be sure that two lines @define-color must be exists
	with open(cssFname, 'r', encoding='utf-8') as file:
		data = file.read()
		data = data.replace(search_primary_color, replace_primary_color)
		data = data.replace(search_secondary_color, replace_secondary_color)
	with open(cssFname, 'w', encoding='utf-8') as file:
		file.write(data)

	#write INI file with new colors
	config['COLORS']['hexprimary'] = replace_primary_color
	config['COLORS']['hexsecondary'] = replace_secondary_color
	config['COLORS']['rgbaprimary'] = replace_rgba_color
	config.write(open(iniFname, 'w', encoding='utf-8'))

def apply_theme():
	# apply new colors on the fly using dbus-send command (gnome v46  tested)
	# gnome shell session must be in unsafe mode
	# use  this extensions to temporary set gs in unsafe mode while using this script
	#
	#  https://github.com/linushdot/unsafe-mode-menu
	#
	os.system("dbus-send --session --dest=org.gnome.Shell --print-reply --type=method_call /org/gnome/Shell org.gnome.Shell.Eval string:'Main.loadTheme(); ' > /dev/null")
	# final greetings
	#print ('')
	print (f"{colors.reset}{colors.bold}{colors.fg.lightgreen}[i] All done. Enjoy your new gnome-shell accent color...{colors.reset}")
	print ('')

# main program
def main():
	#os.system('clear')
	
	# parse arguments
	if checkColors:
		check_colors()

	elif listColors:
		read_all_files()
		print_matrix_with_indices(colors_list, nr_of_rows)
		get_current_schema()

	elif sortColors:
		colors_list.sort()
		read_all_files()
		print_matrix_with_indices(colors_list, nr_of_rows)
		get_current_schema()

	else:
		read_all_files()
		if not applyColors:
			print_matrix_with_indices(colors_list, nr_of_rows)
		get_current_schema()
		interactive_color_selection()
		write_all_files()
		apply_theme()

	# exit program
	sys.exit(0)

if __name__ == '__main__':
	main()