from flask import Flask, request, render_template
import formulas

app = Flask(__name__)

logged_in = True # Change this depending on whether the user is logged in (for later)
@app.route('/')
def index():
    return render_template('home.html',login = logged_in)

@app.route('/start')
def start():
    return render_template('start.html',login = logged_in)

@app.route('/retirement')
def retirement():
    return render_template('retirement.html',login = logged_in)

@app.route('/mortgage')
def mortgage():
    return render_template('mortgage.html',login = logged_in)

@app.route('/mortgage', methods=['POST'])
def mortgage_post():
    rate_percentage = float(request.form['rate_percentage'])
    number_of_years = float(request.form['number_of_years'])
    principal_amount = float(request.form['principal_amount'])

    userMortgage= formulas.Mortgage(rate_percentage,number_of_years,principal_amount)
    userMonthly_Payment = int(userMortgage.monthly_payment())
    userTotal_Interest_Paid = int(userMortgage.total_interest_paid())

    return render_template('mortgage_result.html', userMonthly_Payment=userMonthly_Payment,
                                                    userTotal_Interest_Paid=userTotal_Interest_Paid)

@app.route('/car_payment')
def car_payment():
    return render_template('car_payment.html',login = logged_in)

if __name__ == '__main__':
    app.run(debug=True)
