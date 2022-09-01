from webapp.models import Appliance, Brand
from webapp import app
import os
import json

def calculate(appliances):
    calculations = {}
    for appl in appliances:
        w_to_kw = lambda w: w / 1000
        kw_to_kwh = lambda kw: kw * .3
        appliance = Appliance.query.filter_by(name=appl["appliance"],brand=Brand.query.filter_by(name=appl["brand"]).first()).first()
        energy = w_to_kw(appliance.watts * appl["usage"])
        amount = kw_to_kwh(energy)
        calculations[appliance] = {"energy": energy, "amount": amount, "usage": appl["usage"]}
    return calculations

def recommend(appliance, hours):
    def calculate_savables(hours, given_watt):
        day_to_year = 365
        cost_per_kilowatt = 0.0003

        amount = hours * day_to_year
        watt = amount * given_watt
        price = round(watt * cost_per_kilowatt, 2)

        return hours, amount, watt, price

    remark = ""

    if appliance.name == "Television":
        for limit in range(4, 0, -2):
            if hours > limit:
                remark = f"Limit Television to {limit} hours"
                time, amount, watt, price = calculate_savables(limit, appliance.watts)
                break
        if not remark:
            remark = "Good Job!"
            time, amount, watt, price = calculate_savables(0, appliance.watts)    

    elif appliance.name == "Fridge":
        if hours > 0:
            remark = "Changing to a more efficient brand or reducing the temperature can reduce its energy consumption"
            time, amount, watt, price = calculate_savables(hours, appliance.watts)
    
    elif appliance.name == "Air-Conditioner":
        for limit in range(10, 0, -2):
            if hours > limit:
                remark = f"Limit Air-Conditioner to {limit} hours"
                time, amount, watt, price = calculate_savables(limit, appliance.watts)
                break
        if not remark:
            remark = f"Good Job!"
            time, amount, watt, price = calculate_savables(limit, appliance.watts)    

    elif appliance.name == "Washing Machine":
        for limit in range(3, 0, -1):
            if limit == 1:
                remark = 'Decrese the time spent washing per load'
                time, amount, watt, price = calculate_savables(limit, 50)
            if hours > limit:
                remark = f"Decrease the number of times of washing to {limit}"
                time, amount, watt, price = calculate_savables(limit, appliance.watts)
            break
        if not remark:
            remark = f"Good Job!"
            time, amount, watt, price = calculate_savables(limit, appliance.watts)    

    return {"appliance": appliance.name, "brand": appliance.brand.name,
            "time": time, "amount": amount, "watt": watt, "price": price,
            "remark": remark}
    
def get_data(path):
    path = os.path.join(app.root_path, 'static', *path.replace('\\','/').split('/'))
    with open(path, 'r') as f:
        data = json.loads(f.read())
    return data