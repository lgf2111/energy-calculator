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

results = []
@app.route('/calculator', methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        request_form = request.form
        forms = []
        i = 1
        while True:
            appliance = request_form.get(f"appliance-{i}")
            brand = request_form.get(f"brand-{i}")
            usage = request_form.get(f"usage-{i}")
            ticks = request_form.get(f"ticks-{i}")
            if all([appliance, brand, usage, ticks]):
                forms.append({"appliance": appliance, "brand": brand, "usage": int(usage), "ticks": int(ticks)})
                i += 1
            else:
                break
        results.append(forms)
        return redirect(url_for('result'))
    return render_template('calculator.html', title='Calculator')

@app.route("/result")
def result():
    result = results.pop()
    total_energy, total_amount = calculate(result)
    return render_template('result.html', result=result)

# EXPERIMENTAL
@app.route('/before')
def before():
    return render_template('before.html')

@app.route("/after")
def after():
    return render_template('after.html')

@app.route("/loginv2", methods=['GET', 'POST'])
def loginv2():
    form = LoginForm()
    if form.validate_on_submit:
        if form.email.data == "admin@gmail.com" and form.password.data == "password123":
            flash('Login Successful!', 'success')
            return redirect(url_for('admin.index'))
        else:
            flash("Login Failed", 'danger')
    return render_template('loginv2.html', title="Login", form=form)

@app.route("/algo")
def algo():
    from webapp.models import Appliance
    appliances = Appliance.query.all()
    recommendations = []
    for appliance in appliances:
        result = recommend(appliance, 5)
        recommendations.append(result)
    return recommendations
