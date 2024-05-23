#!/usr/bin/python3
#
# @author: Andrea Antolini (https://github.com/Dasnoopy)
# @license: GNU General Public License v3.0
# @link: https://github.com/dasnoopy/MyAwaita-Colors

import os
import sys
import csv
import argparse
import configparser
from colorsys import rgb_to_hls, hls_to_rgb

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

def hex_to_rgb(hex):
	hex = hex.lstrip('#')
	return tuple(int(hex[i:i+2], 16)  for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def adjust_color_lightness(r, g, b, factor):
    h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def lighten_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 + factor)

def darken_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 - factor)

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
		help='check if there are duplicates HEX colors into the color list')

parser.add_argument('-l','--list-colors', action='store_true', dest='list_colors', default=False,
		help='show list of all accent colors with extra info like HEX and RGB values')

parser.add_argument('-a','--apply-colors', action='store', dest='apply_colors',type=checker,
		help='apply a colors schema from 1 to 24 directly')

args = parser.parse_args()

checkColors = args.check_colors
listColors = args.list_colors
applyColors = args.apply_colors


# define global variables
curr_dir = os.getcwd()
iniFname = 'colors.ini'
cssFname = os.path.expanduser('~') + "/.config/gtk-4.0/colors.css"
shellFname = os.path.expanduser('~') + "/.local/share/themes/MyAdwaita-Colors/gnome-shell/gnome-shell.css"
svgFname = os.path.expanduser('~') + "/.local/share/themes/MyAdwaita-Colors/gnome-shell/toggle-on.svg"
config = configparser.ConfigParser()

# All colors MUST be different and in lower case!
# lighter version of accent color are generated using colors conversion functions

accent_colors = ['#c1392b','#cc5500','#e2725b','#38a89d','#5fa777','#367588',
                 '#483d8b','#b57edc','#3584e4','#60924b','#3b7a57','#1f9d55',
                 '#68778c','#3eb489','#856088','#028fc7','#5661b3','#1560bd',
                 '#1f75fe','#ff69b4','#d70751','#de751f','#5e81ac','#384c81']

# get nr of colors 
# for better visualization keep even num of colors (eg. 12, 18, 24, 30, ....)
nr_of_colors = len(accent_colors)
# colors are listed in [nr_of_rows]
nr_of_rows = int(nr_of_colors / 4)

accent_rgb = list()
lighter_rgb = list()
lighter_colors = list()
lum_factor = 0.1

for i in range (nr_of_colors):
	# convert each HEX accent color in RGB 
	accent_rgb.append (hex_to_rgb (accent_colors[i]))

	# create a RGB lighter color from RGB accent color
	lighter_rgb.append (lighten_color (accent_rgb[i][0], accent_rgb[i][1], accent_rgb[i][2], lum_factor))

	# convert lighter RGB to ligher HEX
	lighter_colors.append (rgb_to_hex (lighter_rgb[i][0], lighter_rgb[i][1], lighter_rgb[i][2]))

# finally combine the accent colors and their lighter version
colors_list = list(zip(accent_colors, lighter_colors))

def check_colors():
	# check if colors in list are all differents
	# check for duplicates colors in colors_list
	from collections import defaultdict
	duplicates = False
	_indices = defaultdict(list)

	for index, item in enumerate(accent_colors):
		_indices[item].append(index + 1)

	for key, value in _indices.items():
		if len(value) > 1:
			# Do something when them
			duplicates = True
			print(f"{colors.reset}{colors.fg.yellow}[w] color:",key,"is defined in position:", value,f"{colors.reset}")

	if not duplicates:
			print(f"{colors.reset}{colors.fg.yellow}[i] All",nr_of_colors,"colors are different. No duplicates!",f"{colors.reset}")


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
	#if schema not found between built-in presets , nothing is displayed!
	while True:
		try:
			idx=int ((next(i for i, w in enumerate(colors_list) if search_primary_color in w and search_secondary_color in w) + 1))
			# convert hex color to RGB just to print colors on terminal
			rgb1 = hex_to_rgb(search_primary_color)
			rgb2 = hex_to_rgb(search_secondary_color)
			R1, G1, B1 = str(rgb1[0]), str(rgb1[1]), str(rgb1[2])
			R2, G2, B2 = str(rgb2[0]), str(rgb2[1]), str(rgb2[2])
			#
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
			R1, G1, B1 = str(rgb1[0]), str(rgb1[1]), str(rgb1[2])
			R2, G2, B2 = str(rgb2[0]), str(rgb2[1]), str(rgb2[2])
			print (f" {colors.reset}{index + 1:02d}: "'\033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm ' + (lista[index][0]) + ' \033[0m\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm ' + (lista[index][1]) + ' \033[0m', end='')
		print('')
	print ('')

def print_info_list(lista: list, righe: int):

	print (f"{colors.reset}"'Info about all available schema colors:')
	print ('')
	# Loop over each row
	for row in range(righe):
		print ('┃',end='')
	# Loop over each column in the current row
		for index in range(row, nr_of_colors, righe):
			# Print elements
			rgb1 = hex_to_rgb(lista[index][0])
			rgb2 = hex_to_rgb(lista[index][1])
			R1, G1, B1 = str(rgb1[0]), str(rgb1[1]), str(rgb1[2])
			R2, G2, B2 = str(rgb2[0]), str(rgb2[1]), str(rgb2[2])
			print (f" {colors.reset}{index + 1:02d}: "'\033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm        ' + ' \033[0m\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm        ' + ' \033[0m' + ' │ ' + lista[index][0] + ' , ' + lista[index][1] + ' │ ' + f"{str(rgb1) : <15}" + ', ' + f"{str(rgb2) : <15}" + ' │ ', end='')
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
		print_matrix_with_indices(colors_list, nr_of_rows)
		check_colors()

	elif listColors:
		read_all_files()
		print_info_list(colors_list, nr_of_colors)
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