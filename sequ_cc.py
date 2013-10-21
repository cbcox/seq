#!/usr/bin/python
#Candace Cox
#main sequ function file
#CL0

import sys

#sequence function
def seq(int1, int2):
	counter = int(int1, base=10)
	while counter <= int(int2, base=10):
		print counter
		'/n'
		counter += 1

#initialize user input variables
int1 = 0
int2 = 0

#take user input
int1, int2 = raw_input("Please enter two numbers: ").split()
'/n'

#check user input for errors
if int1 != 0 and int2 != 0:
	#http://stackoverflow.com/questions/5424716/python-how-to-check-if-input-is-a-number-given-that-input-always-returns-stri/15554564#15554564
	try:
		val = int(int1)
		val2 = int(int2)
	except ValueError:
		print "Please use integers only"
	if int1 < int2:
		seq(int1, int2)
	else:
		print "First integer should be less than second integer"
		sys.exit
else:
	print "Please use two arguments"
	sys.exit

