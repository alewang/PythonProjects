#!/usr/bin/env python
import primes

primeList = [];

primeIndex = 0;
findAgain = True;
while findAgain:
	inp = raw_input("Get next prime (Type 'n' to quit)? ");
	if inp != 'n':
		#Check if we need to generate more primes
		while primeIndex >= len(primeList):
			primes.genPrimes(primeList);
		#Get the next prime in the list
		print primeList[primeIndex];
		primeIndex += 1;
	else:
		findAgain = False;
