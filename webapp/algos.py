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
                time, amount, watt, price = calculate_savables(limit, appliance.watts)
                remark = f"\nHmm, it seems that you are watching TV for {hours} hours. If you stick to {limit} hours, you could save {appliance.watts} kWh, so why not switch to books instead"
                break
        if not remark:
            remark = "Good Job!"
            time, amount, watt, price = calculate_savables(0, appliance.watts)    

    elif appliance.name == "Fridge":
        if hours > 0:
            time, amount, watt, price = calculate_savables(hours, appliance.watts * 0.82)
            watto = watt/1000
            watto = round(watto)
            savesave = watto - appliance.watts
            remark = f"\nYour Fridge is using {watto} kWh right now, if you were to increase the temperature, and decrease the cooling, you could reduce power consumption to {savesave} kWh"
           
    
    elif appliance.name == "Air-Conditioner":
        for limit in range(10, 0, -2):
            if hours > limit:
                time, amount, watt, price = calculate_savables(limit, appliance.watts)
                watto = watt/1000
                watto = round(watto)
                remark = f"\nIt looks like your Air Conditioning expends {watto} kWh. If you used it {limit} hours less, you could save up to ${price} and have a big impact on the environment"
                break
        if not remark:
            remark = f"You are doing a great job but have you ever considered switching to a fan? That might just make your consumption that much less"
            time, amount, watt, price = calculate_savables(limit, appliance.watts)    

    elif appliance.name == "Washing Machine":
        for limit in range(3, 0, -1):
            if limit == 1:
                remark = "\nYour washing rates are pretty good but you could have an even bigger impact if you decrease the time you spend washing each load"
                time, amount, watt, price = calculate_savables(limit, appliance.watts)
            if hours > limit:
                time, amount, watt, price = calculate_savables(limit, appliance.watts * 0.84)
                watto = watt/1000
                watto = round(watto)
                remark = f"\nDid you know that all that washing you do, it takes up {watto} watts of power? If you reduced it to just {limit} times, you could enjoy energy savings of ${price} per annum"
                
            break
        if not remark:
            remark = f"You seem to be doing a great job but you could save a bit more if you try to make your clothes last"
            time, amount, watt, price = calculate_savables(limit, appliance.watts * 0.95)    

    return {"appliance": appliance.name, "brand": appliance.brand.name,
            "time": time, "amount": amount, "watt": watt, "price": price,
            "remark": remark}
    
def cal1(x):
    height = (x * 100) + 100 

def cal2(x):
    width = (x * 75) + 125

           

def get_data(path):
    data =[{ "Key": "2005", "Value": "35489.3" },{ "Key": "2006", "Value": "36801.8" },{ "Key": "2007", "Value": "38304.9" },{ "Key": "2008", "Value": "38986.9" },{ "Key": "2009", "Value": "38822.9" },{ "Key": "2010", "Value": "42251.7" },{ "Key": "2011", "Value": "43007.1" },{ "Key": "2012", "Value": "44200.7" },{ "Key": "2013", "Value": "44948.8" },{ "Key": "2014", "Value": "46403" },{ "Key": "2015", "Value": "47513.9" },{ "Key": "2016", "Value": "48623.1" },{ "Key": "2017", "Value": "49637.8" },{ "Key": "2018", "Value": "50438.2" },{ "Key": "2019", "Value": "51713.3" },{ "Key": "2020", "Value": "50760.5" }]
    return data
