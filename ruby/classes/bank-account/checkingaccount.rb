#!/usr/bin/env ruby

require './account'

class CheckingAccount < Account
	def initialize(amount, allowDebt)
		super(amount)
		@allowDebt = allowDebt == true 
	end

	def debit(amount)
		if !@allowDebt && amount > @amount
			return @amount
		end
		
		super.debit(amount)
	end
end
