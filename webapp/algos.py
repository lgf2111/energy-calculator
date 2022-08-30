from webapp.models import appliance, brand


print("Welcome to Energy Calculato\nPlease Enter the Hours and Brand based on the appliance: ")
totalenergy = 0


def calculate(tv, fridge, aircon, wm):
    tv = (tv.watts * tv.hours) * 365
    fridge = (fridge.watt * fridge.hours) * 365
    aircon = (aircon.watt * aircon.hours) * 365
    wm = (wm.watt * wm.hours) * 365
    totalenergy = tv + fridge + aircon + wm
    totalenergy = totalenergy/1000
    print(totalenergy, "kwh per annum")
    totalamt = totalenergy * 0.30
    print("You spent ", totalamt)
