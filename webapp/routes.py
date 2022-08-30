from webapp import app, db
from flask import render_template, redirect, url_for, flash
from webapp.forms import calculatorForm

@app.route('/')
@app.route('/home')
def home():
    form = calculatorForm
    return render_template('home.html', title='Energy Calculator', form=form)