#!/usr/bin/env ruby

def main()
	errorLimit = get_input()
	approxe = calculateE(errorLimit)
	puts "Approximate value of e: #{approxe}"
end

def factorial(num)
	if num < 0
		return -1
	end

	factorial = 1;
	if num == 0
		return factorial
	end

	counter = 1
	while counter <= num
		factorial *= counter
		counter += 1
	end
	return factorial
end

def get_input()
	print "Enter decimals of accuracy desired (no larger than 15): "
	input = gets

	decimals = input.to_i;
	if decimals == 0 || decimals < 0
		puts "Enter a valid, non-zero natural number for the number of decimals to calculate to."
		return 0
	end

	errorLimit = 10 ** (-decimals)
end

def calculateE(errorLimit)
	if errorLimit <= 0
		return 0
	end

	e = 0.0
	index = 0
	error = 2 * errorLimit
	factorial = factorial(0)
	while error > errorLimit
		term = 1.0 / factorial
		e += term

		index += 1
		factorial *= index

		#There is some inaccuracy in using the term as
		#the error itself, but it's not really a big
		#deal.
		error = term
	end
	return e
end

main
