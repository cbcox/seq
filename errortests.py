#!/usr/bin/python
#Candace Cox
#Error test file

import sequ_cc

#test if there are two arguments
arg_test = sequ_cc.seq(9)

if arg_test != "Please use two arguments":
	print "false" 
else:
	print "true"

#test if arguments are integers
int_test = sequ_cc.seq(bob, spike)

if int_test != "Please use integers only":
	print "false"
else:
	print "true"

#test if the arguments are in sequential order
greaterint_test = sequ_cc.seq(7,1)

if greaterint_test != "First integer should be less than second integer":
	print "false"
else:
	print "true"
