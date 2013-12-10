#!/usr/bin/python
#Candace Cox
#main sequ function file
#CL3 and CL4

import string
import sys
import argparse
import roman

#Global Variables
print_array = []
alpha_lower = string.ascii_lowercase
alpha_upper = string.ascii_uppercase

#---------Functions--------
#sequence function
def seq(x, y):
	xnew = int(x)
	ynew = int(y)
	if xnew%1 == 0:
		counter = int(x)
	else:
		counter = xnew
	if ynew%1 == 0:
		y = int(y)
	while counter <= ynew:
		print_array.append(counter)
		counter += 1

#array print function
def printseq(print_array):
	print ('\n'.join(map(str,(print_array)))) 

#format function
def format():
	curr_arg = args.format
	if args.format == "%a":
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = hex(int(tempint)) 
			print_array[int(i)-1] = newint

	if args.format == "%e":
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = "{:e}".format(float(tempint)) 
			print_array[int(i)-1] = newint
		
	if str(args.format).endswith('f'):
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = curr_arg % tempint 
			print_array[int(i)-1] = newint
		
	if str(args.format).endswith('g'):
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = curr_arg % tempint 
			print_array[int(i)-1] = newint
	
	if args.format == "%A":
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = "0x%X" % tempint 
			print_array[int(i)-1] = newint

	if args.format == "%E":
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = "{:E}".format(float(tempint)) 
			print_array[iint(i)-1] = newint
		
	if str(args.format).endswith('F'):
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = curr_arg % tempint 
			print_array[int(i)-1] = newint
	
	if str(args.format).endswith('G'):
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = curr_arg % tempint 
			print_array[int(i)-1] = newint
	
#equalwidth function
def equalwidth():
	fillnum = len(str(args.y))
	for pi in print_array:
		if len(str(pi)) < fillnum:
			tempint = print_array[int(pi)-1]
			newint = str(tempint).zfill(fillnum)
			print_array[int(pi)-1] = newint

#seperator function
def seperator():
	for s in args.seperator:
		print (str(s).join(map(str,(print_array))))

#words function
def words():
	print (" ".join(map(str,(print_array))))

#pad function
def pad():
	fill_len = len(str(args.y))
	for s in args.pad:
		for i in print_array:
			tempint = print_array[int(i)-1]
			newint = (str(i)).rjust((fill_len+3), s)
			print_array[int(i)-1] = newint
	print ('\n'.join(map(str,(print_array)))) 


#pad-spaces function
def padspaces():
	fill_len = len(str(args.y))
	for i in print_array:
		#adds spaces between integers in array
		tempint = print_array[int(i)-1]
		newint = (str(i)).rjust((fill_len+3), ' ')
		print_array[int(i)-1] = newint
	print ('\n'.join(map(str,(print_array))))

#format-word function
def formatword():
	print args.formatword
	#prints long integer sequences
	if args.formatword == ('arabic'):
			newx = long(args.x)
			newy = long(args.y)
			if not args.z:
				newz = 1
			else:
				newz = long(args.z[0]);
			while newx <= newy:
				print newx
				newx += newz
			sys.exit()

	#print sequence of floats
	if args.formatword == ('floating'):
			floatx = float(args.x)
			floaty = float(args.y)
			if not args.z:
				floatz = 1
			else:
				floatz = float(args.z[0]);
			while floatx <= floaty:
				print floatx
				floatx += floatz
			sys.exit()

	#prints letters in the range specified by the command line args
	if args.formatword == ('alpha'):
			lalphax = ord(args.x)
			lalphay = ord(args.y)
			if not args.z:
				lcounter = 1
			else:
				lcounter = int(args.z[0])
			for number in xrange(lalphax, lalphay+lcounter):
				print chr(number)
			sys.exit()

	#same as alpha except for adding .upper() to print
	if args.formatword == ('ALPHA'):
			ualphax = ord(args.x)
			ualphay = ord(args.y)
			if not args.z:
				ucounter = 1
			else:
				ucounter = int(args.z[0])
			for number in xrange(ualphax, ualphay+ucounter):
				print (chr(number).upper())
			sys.exit()

	if args.formatword == ('roman'):
			roman_start = args.x
			roman_end = args.y
			int_start = roman.fromRoman(roman_start.upper())
			int_end = roman.fromRoman(roman_end.upper())
			print roman_start.lower()
			while int_start < int_end:
				int_start += 1
				roman_start = roman.toRoman(int_start)
				print roman_start.lower()
			
			sys.exit()

	if args.formatword == ('ROMAN'):
			roman_start = args.x
			roman_end = args.y
			int_start = roman.fromRoman(roman_start.upper())
			int_end = roman.fromRoman(roman_end.upper())
			print roman_start
			while int_start < int_end:
				int_start += 1
				roman_start = roman.toRoman(int_start)
				print roman_start
			
			sys.exit()

#integer tests for flags that use ints
def int_test():
	#check if input is integer
	try:
		int(args.x)
		int(args.y)
	except ValueError:
		print "Please use integers or specify -F for format-word"
	#check input for ascending order
	if int(args.x) > int(args.y):
		print "First integer should be less than second integer"
		sys.exit
	else:
		seq(args.x, args.y)


#------Main Driver------
#command line parser
parser = argparse.ArgumentParser(description='Command line sequence arguments.')

#add command line arguments to parser
parser.add_argument('-v', '--version', action='version', version='%(prog)s CL1')
parser.add_argument('-f', '--format', action="store", dest="format")
parser.add_argument('-w', '--equal-width', action="store_true", dest="equalwidth", default=False)
parser.add_argument('-s', '--seperator', action="store", dest="seperator", nargs=1)
parser.add_argument("x")
parser.add_argument("y")
parser.add_argument("z", nargs='*')
parser.add_argument('-W', '--words', action="store_true", dest="words", default=False)
parser.add_argument('-p', '--pad', action="store", dest="pad")
parser.add_argument('-P', '--pad-spaces', action="store_true", dest="padspaces", default=False)
parser.add_argument('-F', '--format-word', dest="formatword", action="store", choices=['arabic', 'floating', 'alpha', 'ALPHA', 'roman', 'ROMAN'])

args = parser.parse_args()

#check for flags used
if args.formatword:
	formatword()
if args.format:
	int_test()
	format()
elif args.equalwidth:
	int_test()
	equalwidth()
if args.seperator:
	int_test()
	seperator()
elif args.words:
	int_test()
	words()
elif args.pad:
	int_test()
	pad()
elif args.padspaces:
	int_test()
	padspaces()
else:
	seq(args.x, args.y)
	printseq(print_array)
