import StringIO
import random
from flask import Flask, request, render_template, make_response

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

logged_in = False # Change this depending on whether the user is logged in (for later)
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
    text = request.form['sadsa']

    return text

@app.route('/car_payment')
def car_payment():
    return render_template('car_payment.html',login = logged_in)

@app.route('/plot.png')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

if __name__ == '__main__':
    app.run(debug=True)
