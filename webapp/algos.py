def calculate(television, fridge, air_conditioner, washing_machine, hours):
    television = (television.watts * hours["television"])
    fridge = (fridge.watts * hours["fridge"])
    air_conditioner = (air_conditioner.watts * hours["air_conditioner"])
    washing_machine = (washing_machine.watts * hours["washing_machine"])
    total_energy = television + fridge + air_conditioner + washing_machine
    total_energy = total_energy / 1000
    total_amount = total_energy * 0.30
    return total_energy, total_amount


def recommend(appliance, hours):
    def calculate_savables(hours, given_watt):
        day_to_year = 365
        cost_per_kilowatt = 0.0003

        amount = hours * day_to_year
        watt = amount * given_watt
        price = watt * cost_per_kilowatt

        return hours, amount, watt, price


    if appliance.name == "Television":
        if hours > 4:
            remark = "Limit TV to 4 hours"
            time, amount, watt, price = calculate_savables(4, appliance.watts)

        elif hours > 2:
            remark = "Limit TV to 2 hours"
            time, amount, watt, price = calculate_savables(2, appliance.watts)

        elif hours <= 2:
            remark = "Good Job!"
            time, amount, watt, price = calculate_savables(0, appliance.watts)
    

    elif appliance.name == "Fridge":
        # TODO: shldnt be calculating savables
        if hours > 0:
            remark = "Changing to a more efficient brand or reducing the temperature can reduce its energy consumption"
            time, amount, watt, price = calculate_savables(hours, appliance.watts)
    

    elif appliance.name == "Air-Conditioner":
        if hours > 10:
            remark = "limit aircon to 10 hours"
            time, amount, watt, price = calculate_savables(10, appliance.watts)
            return  {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

        elif hours > 8:
            remark = "limit aircon to 8 hours"
            time, amount, watt, price = calculate_savables(8, appliance.watts)
            return  {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

        elif hours > 6:
            remark = "limit aircon to 6 hours"
            time, amount, watt, price = calculate_savables(6, appliance.watts)
            return  {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

        elif hours > 4:
            remark = "limit aircon to 4 hours"
            time, amount, watt, price = calculate_savables(4, appliance.watts)
            return  {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

        elif hours > 2 :
            remark = "limit aircon to 2 hours"
            time, amount, watt, price = calculate_savables(2, appliance.watts)
            return  {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}

        # TODO: shldnt be calculating savables
        elif hours <= 2:
            remark = "Good Job!"
            time, amount, watt, price = calculate_savables(2, appliance.watts)
            return  {"remark": remark, "time": time, "amount": amount, "watt": watt, "price": price}
    

    elif appliance.name == "Washing Machine":
        if hours > 3:
            remark = "decrease the number of times of washing to 3"
            time, amount, watt, price = calculate_savables(3, appliance.watts)

        elif hours > 2:
            remark = "decrease the number of times of washing to 2"
            time, amount, watt, price = calculate_savables(2, appliance.watts)

        elif hours <= 2:
            remark = "Decrease the time spent washing per load"
            time, amount, watt, price = calculate_savables(2, 50)

    return {"appliance": appliance.name, "brand": appliance.brand.name,
            "time": time, "amount": amount, "watt": watt, "price": price}
    