#!/usr/bin/env scala

def factor(number: Int): List[Int] = {
	if(number == 1) {
		val myList = List(1);
		return myList;
	}

	val intBelowRoot = getLargestIntBelowRoot(number);
	val myPrimes = getPrimesUpTo(intBelowRoot);
	var primeFactors: List[Int] = List();

	var primeIndex = 0;
	var factoredNumber = number;
	while(primeIndex < myPrimes.length) {
		val primeNum = myPrimes(primeIndex);
		if(factoredNumber % primeNum == 0) {
			factoredNumber /= primeNum;
			primeFactors = primeFactors :+ primeNum;
			primeIndex = 0;
		} else {
			primeIndex += 1;
		}
	}
	return primeFactors;
}

def getLargestIntBelowRoot(n: Int): Int = {
	var index = 0;
	while(index * index < n) {
		index += 1;
	}
	return index;
}

def getPrimesUpTo(n: Int): List[Int] = {
	if(n <= 1) {
		return List();
	}
	var listOfPrimes = List(2);
	var index = 3;
	while(index <= n) {
		var isComposite = false;
		var primeIndex = 0;
		while(primeIndex < listOfPrimes.length && !isComposite) {
			val primeNum = listOfPrimes(primeIndex);
			if(index % primeNum == 0) {
				isComposite = true;
			}
			primeIndex += 1;
		}

		if(!isComposite) {
			listOfPrimes = listOfPrimes :+ index;
		}
		index += 1;
	}

	return listOfPrimes
}

def testGetPrimes() {
	val listOfPrimes = getPrimesUpTo(100);
	for(prime <- listOfPrimes) {
		println(prime);
	}
}

def testFactorization() {
	val num = 420;
	val primeList = factor(num);
	for(prime <- primeList) {
		println(prime);
	}
}

testGetPrimes();
testFactorization();
