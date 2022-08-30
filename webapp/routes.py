from webapp import app, db
from flask import render_template, redirect, url_for, flash
from webapp.forms import CalculatorForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calculator')
def calculator():
    form = CalculatorForm()
    return render_template('calculator.html', title='Energy Calculator', form=form)

@app.route('/before')
def before():
    return render_template('before.html')

@app.route("/after")
def after():
    return render_template('after.html')

