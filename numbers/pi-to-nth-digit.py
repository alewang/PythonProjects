#!/usr/bin/env python
import math

DECIMAL_LIMIT = 10;
decimals = 7;

errorLimit = 10 ** -decimals;
print("The error limit is set to: %.15f" % errorLimit);
pi = 3.0;
factor = 2;
error = errorLimit + 1;
sign = 1;

while error > errorLimit:
    denominator = factor;
    factor += 1;
    denominator *= factor;
    factor += 1;
    denominator *= factor;

    term = sign * 4.0 / denominator;
    pi += term;

    sign *= -1;
    #Just because I'm a bit lazy and I don't want to
    #write more code to calculate the error term
    #I'll use the just calculated term as the
    #error. This works well because the absolute value
    #of each term is less than the absolute value of
    #the term before it, and the series alternates
    error = math.fabs(term);

print(pi);
