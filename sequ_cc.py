#!/usr/bin/python
#Candace Cox
#main sequ function file
#CL1

import sys
import argparse

#Global Variables
print_array = []

#---------Functions--------
#sequence function
def seq(x, y):
	if x%1 == 0:
		counter = int(x)
	else:
		counter = x
	if y%1 == 0:
		y = int(y)
	while counter <= y:
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
		tempint = print_array[int(i)-1]
		newint = (str(i)).rjust((fill_len+3), ' ')
		print_array[int(i)-1] = newint
	print ('\n'.join(map(str,(print_array)))) 


#------Main Driver------
#command line parser
parser = argparse.ArgumentParser(description='Command line sequence arguments.')

#add command line arguments to parser
parser.add_argument('-v', '--version', action='version', version='%(prog)s CL1')
parser.add_argument('-f', '--format', action="store", dest="format")
parser.add_argument('-w', '--equal-width', action="store_true", dest="equalwidth", default=False)
parser.add_argument('-s', '--seperator', action="store", dest="seperator", nargs=1)
parser.add_argument("x", type=float)
parser.add_argument("y", type=float)
parser.add_argument('-W', '--words', action="store_true", dest="words", default=False)
parser.add_argument('-p', '--pad', action="store", dest="pad")
parser.add_argument('-P', '--pad-spaces', action="store_true", dest="padspaces", default=False)

args = parser.parse_args()


#check user input for errors
if args.x != 0 and args.y != 0:
	try:
		val = args.x
		val2 = args.y
	except ValueError:
		print "Please use integers or decimals only"
	if args.x < args.y:
		seq(args.x, args.y)
		if args.format:
			format()
		elif args.equalwidth:
			equalwidth()
		if args.seperator:
			seperator()
		elif args.words:
			words()
		elif args.pad:
			pad()
		elif args.padspaces:
			padspaces()
		else:
			printseq(print_array)
	else:
		print "First integer should be less than second integer"
		sys.exit
else:
	print "Please use two arguments"
	sys.exit

