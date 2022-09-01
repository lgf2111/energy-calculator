import enum
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
    result = results.pop() if results else []
    calculations = calculate(result)
    recommendations = []
    for k in calculations:
        recommendations.append(recommend(k, calculations[k]["usage"]))

    charts = []
    charts.append([[_.name, calculations[_]["energy"]] for _ in calculations])
    charts.append(
        [[{"v": _["appliance"], "f": _["appliance"]}, list(calculations.values())[i]["energy"], _["watt"]/365000] for i, _ in enumerate(recommendations)]
        )
    charts.append([{"v": '', "f": ''}, round(sum(_["amount"] for _ in calculations.values())*365, 2), round(sum(_["price"] for _ in recommendations), 2)])
    return render_template('result.html', calculations=calculations.values(), recommendations=recommendations, charts=charts)

# EXPERIMENTAL
