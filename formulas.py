"""
Flask financial calculation code
"""



class Mortgage():
	def __init__(self, rate_percentage, number_of_years, principal_amount):
		self.r = rate_percentage
		self.n = number_of_years 
		self.p = principal_amount 

	def monthly_payment(self):

		"""
		This is a method for calculating the monthly payment for a home 
		mortgage given the rate percentage, number of years, and principal amount
		"""
		if (self.r==0):
			
			print ("If the interest rate percentage is zero, then the monthly payment is simply the principal divided by the total number of months")
			return (self.p)/(self.n*12)
		else:
			numerator = ((self.r/1200.0)*self.p)
			denominator = (1-(1+(self.r/1200))**-(self.n*12))
			#(1-(1+pow((self.r/1200.0),-(self.n*12))))
			final = numerator/denominator
			return round(final,2)

	def total_interest_paid(self):
		total_payment = self.monthly_payment()*self.n*12-self.p
		return total_payment

	def cumulative_interest(self):
		A = (self.p*(self.r/1200.0))-self.monthly_payment()
		B = ((1+(self.r/1200.0)))**(self.n*12)-1
		return ((A*B)/(self.r/1200.0))+self.monthly_payment()*self.n*12



A = Mortgage(0,1,10)
print A.monthly_payment()






















