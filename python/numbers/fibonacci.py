#!/usr/bin/env python

def fib(nth):
    if nth < 0:
        raise ValueError("Argument passed to fib must be non-negative integer");
    
    twoBehind = 0;
    oneBehind = 1;
    term = 1;
    
    if nth == 0:
        return twoBehind;
    
    if nth == 1:
        return oneBehind;
    
    index = 2;
    while index <= nth:
        term = oneBehind + twoBehind;
        twoBehind = oneBehind;
        oneBehind = term;
        index += 1;
    return term;

index = raw_input("Fibonacci index: ");
numInput = int(index);
listOfNums = [numInput];
counter = 0;
NUMS_TO_INCLUDE = 5;
while counter < NUMS_TO_INCLUDE:
    print fib(numInput + counter);
    counter += 1;

