#!/usr/bin/env ruby

puts "This implementation of the prime factorizer uses the official Ruby Prime library"

require "prime"

inp = $stdin

input = 0
until input > 1
	printf "Enter an integer larger than 1: "
	input = inp.gets
	input = input.to_i
	if input <= 1
		puts "Enter a valid integer."
	end
end

puts "The number entered is " + input.to_s
primeHandler = Prime.instance
factorsList = primeHandler.prime_division(input)
expandedFactorsList = []
for factorSet in factorsList
	prime = factorSet[0]
	exponent = factorSet[1]
	i = 0
	while i < exponent
		expandedFactorsList.push(prime)
		i += 1
	end
end
puts "The prime factors are: " + expandedFactorsList.to_s
