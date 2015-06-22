#!/usr/bin/env python

def genPrimes(listOfPrimes):
    NUM_PRIMES_TO_ADD = 10;
    try:
        primesAdded = 0;
        if len(listOfPrimes) == 0:
            listOfPrimes.append(2);
            primesAdded += 1;
        integer = listOfPrimes[len(listOfPrimes) - 1] + 1;
        while primesAdded < NUM_PRIMES_TO_ADD:
            isPrime = True;
            for num in listOfPrimes:
                remainder = integer % num;
                if remainder == 0:
                    isPrime = False;
                    break;
            if isPrime:
                listOfPrimes.append(integer);
                primesAdded += 1;
            integer += 1;
    except AttributeError as e:
        print "Argument passed to genPrimes must be a list of integers";
        print e;
    return listOfPrimes;

def factor(number):
    if number <= 1:
        raise ValueError("Should be a number greater than 1");
    primeList = [];
    squareOfLast = number - 1;
    while squareOfLast < number:
        genPrimes(primeList);
        lastElemIndex = len(primeList) - 1;
        squareOfLast = primeList[lastElemIndex] ** 2;
    factors = [1];
    index = 0;
    length = len(primeList);
    while index < length:
        remainder = number % primeList[index];
        if remainder == 0:
            number = number / primeList[index];
            factors.append(primeList[index]);
            index = 0;
        else:
            index += 1;
    #After factoring, the remaining number is either
    #a prime number itself (the largest prime), or
    #1
    if number != 1:
        factors.append(number);
    return factors;

def testGenPrimes():
    myList = [];
    genPrimes(myList);
    genPrimes(myList);
    print myList;

def testFactor():
    number = 100;
    factors = factor(number);
    print factors;

if __name__ == "__main__":
    testGenPrimes();
    testFactor();
