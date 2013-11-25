#!/usr/bin/python
#Candace Cox
#CL2 error tests

import sequ_cc

words_test = sequ_cc.words(1 5)

words_string = "1 2 3 4 5"

if words_string == words_string:
	print "false"
else:
	print "true"

pad_test = sequ_cc.pad(: 1 5)

if sequ_cc.print_array[1].startswith(':'):
	print "false"
else:
	print "true"

padspace_test = sequ_cc.padspace(1 5)

if sequ_cc.print_array[1].startswith(' '):
	print "false"
else:
	print "true"


