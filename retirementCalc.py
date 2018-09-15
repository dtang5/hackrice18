import math


class Investment: # About the person
    def __init__(self, current_age, current_balance, retire_age, retire_fund):
        self.years_worked = retire_age - current_age
        self.funds_needed = retire_fund - current_balance
        self.current_balance = current_balance
        self.current_age = current_age
        self.retire_age = retire_age
        self.retire_fund = retire_fund

    # Getter methods
    def get_Age(self):
        return self.current_age

    def compound_interest(self, rate, deposit, year):
        # Rate is a double written as a decimal (IE: 12% -> 0.12)
        rate /= 100
        return self.current_balance * (1 + rate)**year + deposit * (((1 + rate)**year - 1)/rate)

class Portfolio: # About their current portfolio
    def __init__(self, fourone_k, ira, regular, investment, risk):
        #Risk is 1 to 3: 1 = safe, 2 = moderately risky, 3 = very risky
        self.fourone_k = fourone_k
        self.ira = ira
        self.regular = regular
        self.investment = investment
        self.risk = risk

    def decide_my_portfolio(self):
        age = self.investment.get_Age()
        if age

class IRA:
    def __init__(self):


class Retire401K: # 401(k) plan
    def __init__(self, roth, years_left, contribution, salary, total_begin, total_after, employer_match = 0):
        # Limits to the 401K
        # There is a limit to how much you can contribute to your fund yearly. Normally, you are not allowed
        # to contribute more than $18,000 a year to your retirement. If you are above $
        if self.age >= 50:
            self.maximum_contribution = 24500
        else:
            self.maximum_contribution = 18500
        # Roth = True: taxed during deposit False: taxed during withdrawal
        self.roth = roth
        self.salary = salary
        self.contribution = contribution
        self.employer_match = employer_match
        self.total_begin = total_begin
        self.total_after = total_after
        self.years_left = years_left

    def contribution_is_valid(self):
        if self.maximum_contribution < self.contribution:
            return False
        return True

    def compound_interest(self, rate, deposit, year):
        # Yearly
        # Rate is a double written as a decimal (IE: 12% -> 0.12)
        rate /= 100
        return self.current_balance * (1 + rate)**year + deposit * (((1 + rate)**year - 1)/rate)

    def employer_match(self):
        if self.employer_match() == 0.0:
            return 0
        else:
            return self.employer_match() * self.contribution

    def calc_ROI(self):
        if self.total_begin != 0:
            return float((self.total_after - self.total_begin)/self.total_begin)

    def calc_401(self):
        # Monthly calculation
        rate = self.calc_ROI()/12
        return self.current_balance * (1 + rate)**(self.years_left * 12) \
               + self.contribution * ((1 + rate)**(12 * self.years_left - 1)/rate)
