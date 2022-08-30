print("Welcome to Energy Calculato\nPlease Enter the Hours and Brand based on the appliance: ")
totalenergy = 0
def calusage(tv, fridge, aircon, wm):
    global totalenergy
    totalenergy = tv + fridge + aircon + wm
    print(totalenergy, "kwh per annum")

def calamt(totalenergy):
    totalamt = totalenergy * 0.30
    print("You spent ", totalamt)
#TV
print("TV Brand and Usage")
tvbrand = input("TV Brand: ")
tvhours = int(input("TV Hour Usage: "))
if tvbrand == "panasonic":
    tvusage = 110
elif tvbrand == "lg":
    tvusage = 95
elif tvbrand == "philips":
    tvusage = 80
elif tvbrand == "samsung":
    tvusage = 87
elif tvbrand == "others":
    tvusage = 80
tv = (tvusage * tvhours) * 365

#Fridge
print("Fridge Brand and Usage")
fridgebrand = input("Fridge Brand: ")
fridgehours = int(input("Fridge Hour Usage: "))
if fridgebrand == "panasonic":
    fridgeusage = 408
elif fridgebrand == "lg":
    fridgeusage = 275
elif fridgebrand == "hitachi":
    fridgeusage = 160
elif fridgebrand == "samsung":
    fridgeusage = 350
elif fridgebrand == "others":
    fridgeusage = 380
fridge = (fridgeusage * fridgehours) * 365

#AirCon
print("Aircon Brand and Usage")
airconbrand = input("Aircon Brand: ")
airconhours = int(input("Aircon Usage: "))
if airconbrand == "daikin":
    airconusage = 750
elif airconbrand == "mitshubishi":
    airconusage = 725
elif airconbrand == "electrolux":
    airconusage = 775
elif airconbrand == "samsung":
    airconusage = 850
elif airconbrand == "others":
    airconusage = 800
aircon = (airconusage * airconhours) * 365

#washing machine
print("Washing Machine Brand and Usage")
wmbrand = input("Washing Machine Brand: ")
wmhours = int(input("Washing Machine Hour Usage: "))
if wmbrand == "Panasonic":
    wmusage = 750
elif wmbrand == "mitshubishi":
    wmusage = 725
elif wmbrand == "electrolux":
    wmusage = 775
elif wmbrand == "samsung":
    wmusage = 850
elif wmbrand == "others":
    wmusage = 800
wm = (wmusage * wmhours) * 365

#Total Energy 
calusage(tv, fridge, aircon, wm)

#Total money spent
calamt(totalenergy)