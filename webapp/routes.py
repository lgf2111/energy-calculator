from webapp import app, db
from flask import render_template, redirect, url_for, flash, request
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
        print(form)
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

@app.route('/calculator', methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        return request.form
    return render_template('calculator.html', title='Energy Calculator')

@app.route("/result")
def result():
    return render_template('result.html')

# EXPERIMENTAL
