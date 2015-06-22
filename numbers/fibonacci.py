#!/usr/bin/env python

def fib(nth):
    if nth < 0:
        raise ValueError("Argument passed to fib must be non-negative integer");
    
    twoBehind = 0;
    oneBehind = 1;
    term = twoBehind + oneBehind;
    
    if(nth == 0) {
        return twoBehind;
    }
    
    if(nth == 0) {
        return oneBehind;
    }
    index = 2;
    while index <= nth:
        oldTerm = term;
        term = oneBehind + twoBehind;
        twoBehind = oneBehind;
        oneBehind = oldTerm;
        index++;
    return term;
