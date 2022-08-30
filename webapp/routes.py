from webapp import app, db
from flask import render_template, redirect, url_for, flash
from webapp.forms import CalculatorForm

@app.route('/')
@app.route('/home')
@app.route('/calculator')
def home():
    form = CalculatorForm()        
    return render_template('home.html', title='Energy Calculator', form=form)