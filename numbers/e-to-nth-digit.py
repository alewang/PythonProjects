#!/usr/bin/env python
import math;
import sys;
import string;

DECIMAL_LIMIT = 10;
decimals = 0;

#Assume all input is invalid until we finish checking it
readIn = sys.stdin;
print "Enter the number of decimals of accuracy to calculate e (Enter 0 to quit): ",;
invalidInput = True;
while invalidInput:
    lineIn = readIn.readline();
    lineIn = string.strip(lineIn);
    
    isNumber = False;
    isBiggerThanOne = True;
    try:
        decimals = int(lineIn, base=10);
        isNumber = True;
        #We have to check here to determine if the value is 0. If we move the
        #check later, then the if statement to check if the value is larger than
        #1 will take effect and cause us to repeat.
        if decimals == 0:
            exit();
        print "The number of decimals of accuracy is set to: %d" % decimals;
        if decimals < 1:
            isBiggerThanOne = False;
            print "Please enter a value larger than 1. Try again, or enter 0 to quit: ",;
    except ValueError:
        print "That is not a valid number. Try again, or enter 0 to quit: ",;
        isNumber = False;
    invalidInput = (not isNumber) or (not isBiggerThanOne);

errorLimit = 10 ** -decimals;
print("The error limit is set to: %.15f" % errorLimit);
e = 0.0;
error = errorLimit + 1.0;
sign = 1;
factorial = 1;
index = 0;

while error > errorLimit:
    term = 1.0 / factorial;
    e += term;
    index += 1;
    factorial *= index;
    error = 3.0 / factorial;

print(e);
