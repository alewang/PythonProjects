#!/usr/bin/env ruby

module Prime
	def Prime.generatePrimes(startingList)
		if startingList == nil
			startingList = []
		end

		primesAdded = 0
		if startingList.length == 0
			startingList[0] = 2
			primesAdded += 1
		end

		numPrimesToAdd = 10
		integer = startingList[startingList.length - 1]
		position = startingList.length
		while primesAdded < numPrimesToAdd
			isPrime = true
			startingList.each do |prime|
				if integer % prime == 0
					isPrime = false
				end
			end
			if isPrime
				startingList[position] = integer
				position += 1
				primesAdded += 1
			end
			integer += 1
		end
		return startingList
	end

	def Prime.findFactors(number)
		number = number.to_i
		myPrimeList = generatePrimes(nil)
		while myPrimeList[myPrimeList.length - 1] ** 2 < number
			generatePrimes(myPrimeList)
		end

		numPrimes = myPrimeList.length
		factors = []
		while number != 1
			for i in 0...numPrimes
				primeNumber = myPrimeList[i]
				if number % primeNumber == 0
					factors[factors.length] = primeNumber
					number = number / primeNumber
				end
			end
		end
		return factors
	end
end

puts "Module primes is loaded"
if __FILE__ == $0
	myPrimes = []
	Prime.generatePrimes(myPrimes)
	puts myPrimes
	number = 3072
	puts ("Finding prime factors of " + number.to_s)
	puts Prime.findFactors(number)
end
