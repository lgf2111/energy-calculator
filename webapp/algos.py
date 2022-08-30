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
    television, fridge, air_conditioner, washing_machine = hours
    return hours