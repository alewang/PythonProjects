#!/usr/bin/env ruby

require "./prime"

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
factorsList = Prime.findFactors(input)
puts "The prime factors are: " + factorsList.to_s
