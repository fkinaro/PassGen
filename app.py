#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
import argparse


# App to generate secure passwords

# Variable declarations
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','[','}',']','\\','|',':',';',"\'",'\"',',','.','/','?']
alpha = lower + upper + numbers
print(alpha)
helpmsg = """
            Usage:
                app.py -h, app.py --help: to show this help message and exit

                app.py -l=x, length=x: Generate a password of length x and print it to screen.
                x must be a positive integer.

                app.py -l=x file=outfile.txt: Generate a password of length x and append the output to outfile.txt.
                You must have the proper permission to create and modify files
        """

# main code part
#script, length, outfile = argv
# Check the number of arguments supplied:
#if len(argv) < 3:
 #   print (helpmsg)


# Password generation modes
# 0 => alphanumeric
# 1 => alphanumeric + special characters


