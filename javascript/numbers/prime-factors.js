function findFactors(number) {
	var factors = [];
	var primeList = generatePrimes([]);

	for(var lastPrime = primeList[primeList.length - 1];
		lastPrime * lastPrime < number;
		lastPrime = primeList[primeList.length - 1]) {
		generatePrimes(primeList);
	}

	var quotient = number;
	var primeIndex = 0;
	var squareOfPrime = primeList[0] * primeList[0];
	while(squareOfPrime <= quotient && primeIndex < primeList.length) {
		var prime = primeList[primeIndex];
		var isFactor = false;
		if(quotient % prime == 0) {
			factors.push(prime);
			quotient = quotient / prime;
			isFactor = true;
		}

		if(isFactor) {
			primeIndex = 0;
		}
		else {
			primeIndex++;
		}
		squareOfPrime = primeList[primeIndex] * primeList[primeIndex];
	}

	//The final value of quotient should either be '1' or a prime
	//number.
	//We also know that if it is a prime number, it should be
	//the largest prime number in the list because we scanned
	//for all the smaller primes first.
	if(quotient > 1) {
		factors.push(quotient);
	}

	return factors;
}

function generatePrimes(startingList) {
	if(startingList === null || startingList === undefined) {
		return [];
	}

	var primesAdded = 0;
	if(startingList.length == 0) {
		startingList.push(2);
		primesAdded++;
	}

	var NUM_PRIMES_TO_ADD = 10;
	var number;
	for(number = startingList[startingList.length - 1] + 1; primesAdded < NUM_PRIMES_TO_ADD; number++) {
		var isPrime = true;
		for(var index = 0; index < startingList.length; index++) {
			if(number % startingList[index] == 0) {
				isPrime = false;
				break;
			}
		}
		if(isPrime) {
			startingList.push(number);
			primesAdded++;
		}
	}

	return startingList;
}

function testGeneratePrimes() {
	var genPrimes = [];
	generatePrimes(genPrimes);
	generatePrimes(genPrimes);

	var knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71];
	if(genPrimes.length != knownPrimes.length) {
		alert("genPrimes is not the same length as knownPrimes!");
	}

	for(var index = 0; index < knownPrimes.length; index++) {
		var generatedValue = genPrimes[index];
		var knownValue = knownPrimes[index];
		if(generatedValue != knownValue) {
			alert("The generated prime (" + generatedValue + ") is not the same as a known prime (" + knownValue + ").");
		}
	}
}

function testFindFactors() {
	var number = 104;
	var factorsList = [2, 2, 2, 13];
	var calcFactors = findFactors(number);

	if(calcFactors === undefined || calcFactors === null) {
		alert('findFactors() did not return a valid list.');
		return;
	}

	if(calcFactors.length !== factorsList.length) {
		alert('findFactors() did not return the same length list.');
		alert("" + calcFactors);
	}

	for(var index = 0; index < calcFactors.length; index++) {
		if(factorsList[index] !== calcFactors[index]) {
			alert("Index (" + index + ") position has two different values:\n"
				+ "calcFactors: " + calcFactors[index] + "\n"
				+ "factorsList: " + factorsList[index]);
		}
	}
	alert('Test passed');
}
