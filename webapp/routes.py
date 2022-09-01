from webapp import app, db
from flask import render_template, redirect, url_for, flash, request, jsonify
from webapp.forms import CalculatorForm, LoginForm
from webapp.algos import calculate, recommend, get_data
from flask_login import current_user, logout_user
import json

@app.route('/')
@app.route('/home')
def home():
    data = get_data('json/energy.json')
    key, value = [[] for _ in range(2)]
    for d in data:
        key.append(d['Key'])
        value.append(d['Value'])
    return render_template('home.html', key=key, value=value) 

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

glob_forms, glob_results = [[] for _ in range(2)]
@app.route('/calculator', methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        glob_forms.append(request.form)
        return redirect(url_for('calculator_api'), code=307)
    return render_template('calculator.html', title='Calculator')

@app.route("/result")
def result():
    if request.method == "GET":
        result = glob_results.pop() if glob_results else []
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
        return render_template('result.html', calculations=calculations, recommendations=recommendations, charts=charts)

# api
@app.route("/calculator/api", methods=["GET","POST"])
def calculator_api():
    if request.method == "POST":
        request_form = glob_forms.pop()
        forms = []
        total = int(request_form.get("index"))
        for i in range(1, total+1):
            appliance = request_form.get(f"appliance-{i}")
            brand = request_form.get(f"brand-{i}")
            usage = request_form.get(f"usage-{i}")
            ticks = request_form.get(f"ticks-{i}")
            if all([appliance, brand, usage, ticks]):
                forms.append({"appliance": appliance, "brand": brand, "usage": int(usage), "ticks": int(ticks)})
        glob_results.append(forms)
        return redirect(url_for('result'))

    elif request.method == "GET":
        # http://127.0.0.1:5000/calculator/api?appliance-1=Fridge&brand-1=Hitachi&usage-1=5&ticks-1=5
        request_args = request.args
        forms = []
        i = 1
        while True:
            appliance = request_args.get(f"appliance-{i}")
            brand = request_args.get(f"brand-{i}")
            usage = request_args.get(f"usage-{i}")
            ticks = request_args.get(f"ticks-{i}")        
            if all([appliance, brand, usage, ticks]):
                forms.append({"appliance": appliance, "brand": brand, "usage": int(usage), "ticks": int(ticks)})
                i += 1
            else:
                break
        glob_results.append(forms)
        return redirect(url_for('result_api'), code=307)

@app.route("/result/api", methods=["POST", "GET"])
def result_api():
    result =  glob_results.pop() if glob_results else []
    calculations = calculate(result)
    recommendations = []
    for k in calculations:
        recommendations.append(recommend(k, calculations[k]["usage"]))
    return jsonify(recommendations)