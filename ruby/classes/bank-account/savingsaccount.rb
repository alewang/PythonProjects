#!/usr/bin/env ruby

require "./account"

class SavingsAccount < Account
	def initialize(amount, interest)
		super(amount)
		@interest = interest
	end

	def includeInterest
		abs_interest = @amount * @interest
		@amount += abs_interest
	end
end

if $0 == __FILE__
	myAccount = SavingsAccount.new(100, 0.01)
	balance = myAccount.getBalance
	puts "Savings account initialized with $#{balance} at 1% interest"
	myAccount.credit(900)
	balance = myAccount.getBalance
	puts "Savings account now has $#{balance}."
	myAccount.includeInterest
	puts "A period of time has passed, and interest has taken effect"
	puts "The savings account now has $#{myAccount.getBalance}"
	myAccount.debit(1500)
	puts "We took out $1500 from the account. Now we have #{myAccount.getBalance}"
end
