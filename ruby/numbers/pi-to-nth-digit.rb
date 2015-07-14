#!/usr/bin/env ruby
decimals = 15
errorLimit = 10.0 ** (-decimals)
pi = 3
error = errorLimit * 2;
puts "Error limit: #{errorLimit}"

factor1 = 2
factor2 = 3
factor3 = 4
sign = 1

counter = 0
counterLimit = 100000
while error > errorLimit and counter < counterLimit
	denominator = factor1 * factor2 * factor3
	numerator = 4.0
	term = numerator / denominator * sign
	pi += term

	factor1 = factor3
	factor2 = factor1 + 1
	factor3 = factor1 + 2
	counter += 1
	error = term.abs
	sign = sign * -1;
end

puts "The calculated value of pi is: #{pi}. Error: #{error}. Counter: #{counter}"
