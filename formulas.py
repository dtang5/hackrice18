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


class Credit_Card_Payment():

	def __init__(self, APR_percentage, Balance, Payment):

		self.a = APR_percentage
		self.b = Balance
		self.p = Payment

	def payoff_time(self,units):
		"""
		This is a method which returns the time it takes to payoff an input credit card balance with 
		an input APR percentage and an input monthly payment

		https://www.vcalc.com/wiki/KurtHeckman/Credit+Card+Equation
		"""

		percent = self.a/100.0
		numerator = math.log((1+(self.b/self.p)*(1-(1+(percent/365))**30)))
		denominator = math.log(1+(percent/365.0))

		result = ((-1.0/30)*(numerator/denominator))

		if (units.lower() == 'years'):
			return round(result*0.0833,2)
		elif (units.lower() == 'months'):
			return round(result,2)
		elif (units.lower() == 'weeks'):
			return round(result*4.345,2)
		elif (units.lower() == 'days'):
			return round(result*30.417,2)
		else:
			return "Select only years, months, weeks, or days"
	
	def graph_payoff_times():
		



A = Credit_Card_Payment(3,1000, 10)
print A.payoff_time('weeks')



















