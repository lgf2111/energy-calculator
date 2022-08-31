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
            "time": time, "amount": amount, "watt": watt, "price": price}
    