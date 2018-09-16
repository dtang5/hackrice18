# import matplotlib.pyplot as plt

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

    def get_current_balance(self):
        return self.current_balance

    def compound_interest(self, rate, deposit, year):
        # Rate is a double written as a decimal (IE: 12% -> 0.12)
        rate /= 100
        return self.current_balance * (1 + rate)**year + deposit * (((1 + rate)**year - 1)/rate)


class Portfolio: # About their current portfolio
    def __init__(self, fourone_k, investment, risk):
        # Investment is a
        # Risk is 1 to 3: 1 = safe, 2 = moderately risky, 3 = very risky
        self.fourone_k = fourone_k
        # self.ira = ira
        # self.regular = regular
        self.investment = investment
        self.risk = risk


class Retire401K: # 401(k) plan
    def __init__(self, age, years_left, contribution, total_after=0, rate=0, total_begin=0, employer_match=0):
        self.age = age
        self.BELOW_AVERAGE_RATE = 4
        self.AVERAGE_RATE = 6.5 # This is a good yearly ROI for 401K's.
        self.ABOVE_AVERAGE_RATE = 8
        # Limits to the 401K
        if self.age >= 50:
            self.maximum_contribution = 24500
        else:
            self.maximum_contribution = 18500
        # Roth = True: taxed during deposit False: taxed during withdrawal
        self.contribution = contribution
        self.employer_match = employer_match
        self.total_begin = total_begin
        self.total_after = total_after
        # Calculate ROI to use.
        self.rate = rate

        self.years_left = years_left

    def decide_my_portfolio(self):
        # This uses an old rule of thumb to recommend the best portfolio.
        # Returns list [percent stocks, percent bonds]
        if self.age >= 100:
            return [0, 100]
        return [self.age, 100 - self.age]

    def contribution_is_valid(self):
        if self.maximum_contribution < self.contribution:
            return False
        return True

    def compound_interest(self, rate, deposit, year):
        # Yearly
        # Rate is a double written as a decimal (IE: 12% -> 0.12)
        rate /= 100
        return self.total_begin * (1 + rate)**year + deposit * (((1 + rate)**year - 1)/rate)

    def employer_match(self):
        if self.employer_match() == 0.0:
            return 0
        else:
            return self.employer_match() * self.contribution

    def get_bad_rate(self):
        print self.rate
        if self.rate < 0.02:
            return 0
        else:
            return self.rate - 0.02

    def get_good_rate(self):
        if self.rate > 0.98:
            return 1
        else:
            return self.rate + 0.02

    def calc_ROI(self):
        if self.total_begin != 0:
            return float((self.total_after - self.total_begin))/self.total_begin

    def calc_401(self):
        if self.rate == 0:
            return round(self.total_after * (1 + self.rate)**(self.years_left * 12))
        else:
            adjusted_rate = float(self.rate)/(100 * 12)
            return round(self.total_after * (1 + adjusted_rate)**(self.years_left * 12) \
                         + self.contribution * (((1 + adjusted_rate)**(12 * self.years_left ) - 1)/adjusted_rate), 2)


