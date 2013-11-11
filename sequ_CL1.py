#!/usr/bin/python
#Candace Cox
#main sequ function file
#CL1

import sys
import argparse


#------Main Driver------
#command line parser
parser = argparse.ArgumentParser(description='Command line sequence arguments.')

#add command line arguments to parser
parser.add_argument('-v', '--version', action='version', version='%(prog)s CL1')
parser.add_argument('-f', '--format')
parser.add_argument('-w', '--equal-width', action="store_true", dest="equalwidth", default=False)
parser.add_argument('-s', '--seperator', action="store", dest="seperator", nargs=1)
parser.add_argument("x", type=int)
parser.add_argument("y", type=int)

args = parser.parse_args()

print args.x
print args.y

