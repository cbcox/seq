#!/usr/bin/python
#Candace Cox
#Error test file

import sequ_cc

#CL0 Tests:

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

#CL1 Tests:

#equal width
#test different int lengths
tens_test = seq_cc.equalwidth(1,12);

if len(str(tens_test)) == 2:
	print "false"
else:
	print "true"

hundreds_test = seq_cc.equalwidth(1,120);

if len(str(tens_test)) == 3:
	print "false"
else:
	print "true"

thousands_test = seq_cc.equalwidth(1,1200);

if len(str(tens_test)) == 4:
	print "false"
else:
	print "true"

#test floating-point
float_test = seq_cc.equalwidth(1,10.4);

if len(str(tens_test)) == 2:
	print "false"
else:
	print "true"

#seperator
#test different input

string_test = "1<=2<=3<=4<="

string_output = seq_cc.seperator(1,4,"<=")

if string_output == string_test:
	print "false"
else:
	print "true"

multarg_test = "1:y2:y3:y4:y"

multarg_output = seq_cc.seperator(1,4,:y)

if multarg_output == multarg_test:
	print "false"
else:
	print "true"

compop_test = seq_cc.seperator(1,4,>)

if compop_test != "Please use valid input.":
	print "false"
else:
	print "true"
