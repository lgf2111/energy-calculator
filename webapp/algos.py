def calculate(television, fridge, air_conditioner, washing_machine, hours):
    television = (television.watts * hours["television"])
    fridge = (fridge.watts * hours["fridge"])
    air_conditioner = (air_conditioner.watts * hours["air_conditioner"])
    washing_machine = (washing_machine.watts * hours["washing_machine"])
    total_energy = television + fridge + air_conditioner + washing_machine
    total_energy = total_energy / 1000
    total_amount = total_energy * 0.30
    return total_energy, total_amount

def recommend(hours, applicance):
    def calculate_savables(given_hour, given_watt):
        day_to_year = 365
        cost_per_kilowatt = 0.3

        amount = given_hour * day_to_year
        watt = amount * given_watt
        price = watt * cost_per_kilowatt

        return time, amount, watt, price

    recommendations = {}
    television, fridge, air_conditioner, washing_machine = [{} for _ in range(4)]

    if hours["television"] > 4:
        remark = "Limit TV to 4 hours"
        time, amount, watt, price = calculate_savables(4, applicance.watt)
        television = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    elif hours["television"] > 2:
        remark = "Limit TV to 2 hours"
        time, amount, watt, price = calculate_savables(2, applicance.watt)
        television = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    elif hours["television"] <= 2:
        remark = "Good Job!"
        time, amount, watt, price = calculate_savables(0, applicance.watt)
        television = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    recommendations["television"] = television
    

    # TODO: shldnt be calculating savables
    if hours["fridge"] > 0:
        remark = "Changing to a more efficient brand or reducing the temperature can reduce its energy consumption"
        time, amount, watt, price = calculate_savables(hours["fridge"], applicance.watt)
        fridge = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}
    
    recommendations["fridge"] = fridge

    if hours["air_conditioner"] > 10:
        remark = "limit aircon to 10 hours"
        time, amount, watt, price = calculate_savables(10, applicance.watt)
        air_conditioner = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    elif hours["air_conditioner"] > 8:
        remark = "limit aircon to 8 hours"
        time, amount, watt, price = calculate_savables(8, applicance.watt)
        air_conditioner = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    elif hours["air_conditioner"] > 6:
        remark = "limit aircon to 6 hours"
        time, amount, watt, price = calculate_savables(6, applicance.watt)
        air_conditioner = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    elif air_conditioner > 4:
        remark = "limit aircon to 4 hours"
        time, amount, watt, price = calculate_savables(4, applicance.watt)
        air_conditioner = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    elif hours["air_conditioner"] > 2 :
        remark = "limit aircon to 2 hours"
        time, amount, watt, price = calculate_savables(2, applicance.watt)
        air_conditioner = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    # TODO: shldnt be calculating savables
    elif hours["air_conditioner"] <= 2:
        remark = "Good Job!"
        time, amount, watt, price = calculate_savables(2, applicance.watt)
        air_conditioner = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    recommendations["air_conditioner"] = air_conditioner
    

    if hours["washing_machine"] > 3:
        remark = "decrease the number of times of washing to 3"
        time, amount, watt, price = calculate_savables(3, applicance.watt)
        recommendation = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    if hours["washing_machine"] > 2:
        remark = "decrease the number of times of washing to 2"
        time, amount, watt, price = calculate_savables(2, applicance.watt)
        recommendation = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    if hours["washing_machine"] <= 2:
        remark = "Decrease the time spent washing per load"
        time, amount, watt, price = calculate_savables(2, 50)
        recommendation = {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

    recommendations["washing_machine"] = washing_machine

    return recommendations