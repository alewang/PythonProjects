#!/usr/bin/env ruby

#Let's try something new this time
#Let's read in our arguments
#through the command line

def main()
	if ARGV.length != 1
		puts "Usage: #{$0} index_of_fibonacci_number"
		exit(1)
	end

	begin
		input = Integer(ARGV[0])
		rescue ArgumentError => error
			puts "Input argument must be natural number"
			exit 1
	end

	puts "The Fibonacci number at position #{input} is #{fib(input)}"
end

def fib(n)
	if n == 0
		return 0
	end

	if n == 1
		return 1
	end

	behindBy1 = 1
	behindBy2 = 0

	index = 1
	while index < n
		term = behindBy1 + behindBy2
		index += 1
		behindBy2 = behindBy1
		behindBy1 = term
	end
	return term
end

main
