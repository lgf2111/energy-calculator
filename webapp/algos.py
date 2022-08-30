def calculate(television, fridge, air_conditioner, washing_machine, hours):
    television = (television.watts * hours["television"])
    fridge = (fridge.watts * hours["fridge"])
    air_conditioner = (air_conditioner.watts * hours["air_conditioner"])
    washing_machine = (washing_machine.watts * hours["washing_machine"])
    total_energy = television + fridge + air_conditioner + washing_machine
    total_energy = total_energy / 1000
    total_amount = total_energy * 0.30
    return total_energy, total_amount

def recommend(hours):
    television, fridge, air_conditioner, washing_machine = hours.values()
    recommendations = {}
    #tv
    if television > 4:
        recommendations["television"] = "limit tv to 4 hours"
        # savetime = hours - 4
        # saveamt = savetime * 365
        # savewatt = saveamt * television.watt
        # saveprice = savewatt * 0.3
    elif television > 2:
        recommendations["television"] =  "limit hours to 2 hours"
        # savetime = hours - 2
        # saveamt = savetime * 365
        # savewatt = saveamt * television.watt
        # saveprice = savewatt * 0.3
    elif television < 2:
        recommendations["television"] = "Great Job!"
    #fridge
    if fridge != 0:
        recommendations["fridge"] = "Changing to a more efficient brand or reducing the temperature can reduce its energy consumption"
        # saveamt = savetime * 365
        # savewatt = saveamt * 30
        # saveprice = savewatt * 0.3
    #aircon
    if air_conditioner > 10:
        recommendations["air_conditioner"] = "limit aircon to 8 hours"
        # savetime = hours - 10
        # saveamt = savetime * 365
        # savewatt = saveamt * air_conditioner.watt
        # saveprice = savewatt * 0.3
    elif air_conditioner > 8:
        recommendations["air_conditioner"] = "limit aircon to 6 hours"
        # savetime = hours - 6
        # saveamt = savetime * 365
        # savewatt = saveamt * air_conditioner.watt
        # saveprice = saveamt * 0.3
    elif air_conditioner > 6:
        recommendations["air_conditioner"] = "limit aircon to 4 hours"
        # savetime = hours - 6
        # saveamt = savetime * 365
        # savewatt = saveamt * air_conditioner.watt
        # saveprice = savewatt * 0.3
    elif air_conditioner > 4:
        recommendations["air_conditioner"] = "limit aircon to 2 hours"
        # savetime = hours - 4
        # saveamt = savetime * 365
        # savewatt = saveamt * air_conditioner.watt
        # saveprice = savewatt * 0.3
    elif air_conditioner > 2 :
        recommendations["air_conditioner"] = "limit aircon to 2 hours"
        # savetime = hours - 2
        # saveamt = savetime * 365
        # savewatt = saveamt * air_conditioner.watt
        # saveprice = savewatt * 0.3
    elif air_conditioner <= 2:
        recommendations["air_conditioner"] = "Good Job!"
    #wm
    if washing_machine > 3:
        recommendations["washing_machine"] = "decrease the number of times of washing to 3"
        # savetime = hours - 3
        # saveamt = savetime * 365
        # savewatt = saveamt * washing_machine.watt
        # saveprice = savewatt * 0.3
    if washing_machine > 2:
        recommendations["washing_machine"] = "decrease the number of times of washing to 2"
        # savetime = hours - 2
        # saveamt = savetime * 365
        # savewatt = saveamt * washing_machine.watt
        # saveprice = savewatt * 0.3
    if washing_machine <= 2:
        recommendations["washing_machine"] = "decrease the time spent washing per load"
        # saveamt = savetime * 365
        # savewatt = saveamt * 50
        # saveprice = savewatt * 0.3
    return recommendations