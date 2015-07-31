#!/usr/bin/env ruby

class Account
	def initialize(amount)
		@amount = amount
	end

	def debit(amount)
		amount = Integer(amount)
		@amount -= amount
	end

	def credit(amount)
		amount = Integer(amount)
		@amount += amount
	end

	def getBalance
		@amount
	end
end
