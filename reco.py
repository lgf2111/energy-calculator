usage = 0
watt = 100
#tv
if usage > 4:
    print("limit tv to 4 hours")
    savetime = usage - 4
    saveamt = savetime * 365
    savewatt = saveamt * watt
    saveprice = savewatt * 0.3
elif usage > 2:
    print("limit usage to 2 hours")
    savetime = usage - 2
    saveamt = savetime * 365
    savewatt = saveamt * watt
    saveprice = savewatt * 0.3
#fridge
if usage != 0:
    print("Changing to a more efficient brand or reducing the temperature can reduce its energy consumption") 
    saveamt = savetime * 365
    savewatt = saveamt * 30
    saveprice = savewatt * 0.3
#aircon
if usage > 10:
    print("limit aircon to 8 hours")
    savetime = usage - 10
    saveamt = savetime * 365
    savewatt = saveamt * watt
    saveprice = savewatt * 0.3
elif usage > 8:
    print("limit aircon to 6 hours")
    savetime = usage - 6
    saveamt = savetime * 365
    saveprice = saveamt * 0.3
elif usage > 6:
    print("limit aircon to 4 hours")
    savetime = usage - 6
    saveamt = savetime * 365
    savewatt = saveamt * watt
    saveprice = savewatt * 0.3
elif usage > 4:
    print("increase aircon temperature")
    saveamt = savetime * 365
    savewatt = saveamt * 100
    saveprice = savewatt * 0.3
#wm
if usage > 3:
    print("decrease the number of times of washing to 3")
    savetime = usage - 3
    saveamt = savetime * 365
    savewatt = saveamt * watt
    saveprice = savewatt * 0.3
if usage > 2:
    print("decrease the number of times of washing to 2")
    savetime = usage - 2
    saveamt = savetime * 365
    savewatt = saveamt * watt
    saveprice = savewatt * 0.3
if usage < 2:
    print("decrease the time spent washing")
    saveamt = savetime * 365
    savewatt = saveamt * 50
    saveprice = savewatt * 0.3