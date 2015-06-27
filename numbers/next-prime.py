#!/usr/bin/env python

import primes

primeList = [];

index = 0;
keepGoing = True;
while keepGoing:
	inp = raw_input("Enter q to quit: ");
	if inp == 'q':
		keepGoing = False;
	else:
		if index == len(primeList):
			primes.genPrimes(primeList);
		print primeList[index];
		index += 1;

print "Program complete. Exiting..."
