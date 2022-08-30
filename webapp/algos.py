from re import A


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
    
    if television > 4:
        recommendations["television"]["reco"] = "limit tv to 4 hours"
        savetime = television - 4
        saveamt = savetime * 365
        savewatt = saveamt * television.watt
        saveprice = savewatt * 0.3
        recommendations["television"]["savetime"] = savetime
        recommendations["television"]["saveamt"] = saveamt
        recommendations["television"]["savewatt"] = savewatt
        recommendations["television"]["saveprice"] = saveprice
    elif television > 2:
        recommendations["television"]["reco"] = "limit tv to 4 hours"
        savetime = television - 2
        saveamt = savetime * 365
        savewatt = saveamt * television.watt
        saveprice = savewatt * 0.3
        recommendations["television"]["savetime"] = savetime
        recommendations["television"]["saveamt"] = saveamt
        recommendations["television"]["savewatt"] = savewatt
        recommendations["television"]["saveprice"] = saveprice
    elif television <= 2:
        recommendations["television"]["reco"] = "Great Job!"
    
    if fridge != 0:
        recommendations["fridge"]["reco"] = "Changing to a more efficient brand or reducing the temperature can reduce its energy consumption"
        saveamt = fridge * 365
        savewatt = saveamt * 30
        saveprice = savewatt * 0.3
        recommendations["fridge"]["saveamt"] = saveamt
        recommendations["fridge"]["savewatt"] = savewatt
        recommendations["fridge"]["saveprice"] = saveprice
    
    if air_conditioner > 10:
        recommendations["air_conditioner"]["reco"] = "limit aircon to 8 hours"
        savetime = air_conditioner - 10
        saveamt = savetime * 365
        savewatt = saveamt * air_conditioner.watt
        saveprice = savewatt * 0.3
        recommendations["air_conditioner"]["savetime"] = savetime
        recommendations["air_conditioner"]["saveamt"] = saveamt
        recommendations["air_conditioner"]["savewatt"] = savewatt
        recommendations["air_conditioner"]["saveprice"] = saveprice
    elif air_conditioner > 8:
        recommendations["air_conditioner"]["reco"] = "limit aircon to 6 hours"
        savetime = air_conditioner - 6
        saveamt = savetime * 365
        savewatt = saveamt * air_conditioner.watt
        saveprice = saveamt * 0.3
        recommendations["air_conditioner"]["savetime"] = savetime
        recommendations["air_conditioner"]["saveamt"] = saveamt
        recommendations["air_conditioner"]["savewatt"] = savewatt
        recommendations["air_conditioner"]["saveprice"] = saveprice
    elif air_conditioner > 6:
        recommendations["air_conditioner"]["reco"] = "limit aircon to 4 hours"
        savetime = air_conditioner - 6
        saveamt = savetime * 365
        savewatt = saveamt * air_conditioner.watt
        saveprice = savewatt * 0.3
        recommendations["air_conditioner"]["savetime"] = savetime
        recommendations["air_conditioner"]["saveamt"] = saveamt
        recommendations["air_conditioner"]["savewatt"] = savewatt
        recommendations["air_conditioner"]["saveprice"] = saveprice
    elif air_conditioner > 4:
        recommendations["air_conditioner"]["reco"] = "limit aircon to 2 hours"
        savetime = air_conditioner - 4
        saveamt = savetime * 365
        savewatt = saveamt * air_conditioner.watt
        saveprice = savewatt * 0.3
        recommendations["air_conditioner"]["savetime"] = savetime
        recommendations["air_conditioner"]["saveamt"] = saveamt
        recommendations["air_conditioner"]["savewatt"] = savewatt
        recommendations["air_conditioner"]["saveprice"] = saveprice
    elif air_conditioner > 2 :
        recommendations["air_conditioner"]["reco"] = "limit aircon to 2 hours"
        savetime = air_conditioner - 2
        saveamt = savetime * 365
        savewatt = saveamt * air_conditioner.watt
        saveprice = savewatt * 0.3
        recommendations["air_conditioner"]["savetime"] = savetime
        recommendations["air_conditioner"]["saveamt"] = saveamt
        recommendations["air_conditioner"]["savewatt"] = savewatt
        recommendations["air_conditioner"]["saveprice"] = saveprice
    elif air_conditioner <= 2:
        recommendations["air_conditioner"]["reco"] = "Good Job!"
    
    if washing_machine > 3:
        recommendations["washing_machine"]["reco"] = "decrease the number of times of washing to 3"
        savetime = washing_machine - 3
        saveamt = savetime * 365
        savewatt = saveamt * washing_machine.watt
        saveprice = savewatt * 0.3
        recommendations["washing_machine"]["savetime"] = savetime
        recommendations["washing_machine"]["saveamt"] = saveamt
        recommendations["washing_machine"]["savewatt"] = savewatt
        recommendations["washing_machine"]["saveprice"] = saveprice
    if washing_machine > 2:
        recommendations["washing_machine"]["reco"] = "decrease the number of times of washing to 2"
        savetime = washing_machine - 2
        saveamt = savetime * 365
        savewatt = saveamt * washing_machine.watt
        saveprice = savewatt * 0.3
        recommendations["washing_machine"]["savetime"] = savetime
        recommendations["washing_machine"]["saveamt"] = saveamt
        recommendations["washing_machine"]["savewatt"] = savewatt
        recommendations["washing_machine"]["saveprice"] = saveprice
    if washing_machine <= 2:
        recommendations["washing_machine"]["reco"] = "Decrease the time spent washing per load"
        saveamt = 2 * 365
        savewatt = saveamt * 50
        saveprice = savewatt * 0.3
        recommendations["washing_machine"]["saveamt"] = saveamt
        recommendations["washing_machine"]["savewatt"] = savewatt
        recommendations["washing_machine"]["saveprice"] = saveprice
    return recommendations, saveamt, savewatt, saveprice