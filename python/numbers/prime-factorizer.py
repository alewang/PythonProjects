#!/usr/bin/env python
import primes
import sys

#The numerical argument which we should be factoring should
#is the first command line argument:
inputNum = None;
try:
    rawArgument = sys.argv[1];
    inputNum = int(rawArgument);
except (IndexError, ValueError):
    print "You must provide an integer argument for this script to factorize!";
    sys.exit(1);

if inputNum is None:
    print "There was an error parsing the input. Exiting...";
    sys.exit(1);

if inputNum < 2:
    print "Enter a integer argument that is larger than 2";
    sys.exit(1);

listOfFactors = primes.factor(inputNum);
print listOfFactors;
