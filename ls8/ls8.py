#!/usr/bin/env python3

"""Main."""


import sys
from cpu import *
cpu = CPU()

# sys.argv.append('C:\\Users\\lizzy\\Documents\\School folder\\CS Projects\\Class assignments\\Computer-Architecture\\ls8\\examples\print8.ls8')
# sys.argv.append('C:\\Users\\lizzy\\Documents\\School folder\\CS Projects\\Class assignments\\Computer-Architecture\\ls8\\examples\mult.ls8')

if len(sys.argv) > 1:
    # print(sys.argv[1], 'sys.argv[1]')
    cpu.load(sys.argv[1])
    cpu.run()

else:
    print("please add a program to run")

    