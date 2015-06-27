#!/usr/bin/env python

class Mortgage:
	"""A class to represent a mortgage"""
	def __init__(self, principal, interestRate):
		self.principal = principal;
		self.rate = interestRate;
	
	def makePayment(self, payment):
		overpaid = 0;
		if(self.principal < payment):
			self.principal = 0;
			overpaid = payment - self.principal;
		else:
			self.principal = self.principal - payment;
		return overpaid;
	
	def addInterest(self):
		self.principal = (1.0 + self.rate) * self.principal;
		return self.principal;
	
	def getPrincipal(self):
		return self.principal;
	
	def getInterestPayment(self):
		return 1.0 * self.principal * self.rate;

mort = Mortgage(5000.0, 0.05);
print "For paying off just the interest, you must pay", mort.getInterestPayment();

monthlyPayments = 1000;
monthsPassed = 0;
while mort.getPrincipal() > 0:
	previousPrincipal = mort.getPrincipal();
	mort.addInterest();
	mort.makePayment(monthlyPayments);
	monthsPassed += 1;
	if mort.getPrincipal() >= previousPrincipal:
		print "You will never be able to pay this off with this sort of payment";
		break;

if mort.getPrincipal() <= 0:
	print "It took you", monthsPassed, "months to pay this off.";
else:
	print "You were not able to pay off the mortgage at all.";
