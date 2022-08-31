from webapp import app, db
from flask import render_template, redirect, url_for, flash
from webapp.forms import CalculatorForm, LoginForm
from webapp.algos import calculate, recommend
from flask_login import current_user, logout_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        if form.email.data == "admin@gmail.com" and form.password.data == "password123":
            flash('Login Successful!', 'success')
            return redirect(url_for('admin.index'))
        else:
            flash("Login Failed", 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    current_user.logout_user
    return redirect('home')

@app.route('/calculator')
def calculator():
    form = CalculatorForm()
    return render_template('calculator.html', title='Energy Calculator', form=form)

@app.route("/result")
def result():
    return render_template('result.html')

# EXPERIMENTAL
@app.route('/before')
def before():
    return render_template('before.html')

@app.route("/after")
def after():
    return render_template('after.html')

@app.route("/loginv2")
def loginv2():
    return render_template('loginv2.html')

@app.route("/algo")
def algo():
    from webapp.models import Appliance
    appliances = Appliance.query.all()
    recommendations = []
    for appliance in appliances:
        result = recommend(appliance, 5)
        recommendations.append(result)
    return recommendations
