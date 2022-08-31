from webapp.algos import calculate, recommend
from webapp.models import Appliance

def test_calculate():
    television = Appliance.query.filter_by(name="Television").first() # 110
    fridge = Appliance.query.filter_by(name="Fridge").first() # 408
    air_conditioner = Appliance.query.filter_by(name="Air-Conditioner").first() # 750
    washing_machine = Appliance.query.filter_by(name="Washing Machine").first() # 660
    hours = {"television": 2, "fridge": 2, "air_conditioner": 2, "washing_machine": 2}
    assert calculate(television, fridge, air_conditioner, washing_machine, hours) == (3.856, 1.1567999999999998)

# def test_recommend():
#     hours = {"television": 2, "fridge": 2, "air_conditioner": 2, "washing_machine": 2}
#     recommendations = recommend(hours)
    
    # assert recommendations == ({"television": {"reco": "Great Job!", "savetime": "", "saveamt": "", "savewatt": "", "saveprice": ""},
    #                             "fridge": {"reco": "Changing to a more efficient brand or reducing the temperature can reduce its energy consumption", "savetime": "", "saveamt": "", "savewatt": "", "saveprice": ""},
    #                           "air_conditioner": {"reco": "Good Job!", "savetime": "", "saveamt": "", "savewatt": "", "saveprice": ""},
    #                             "washing_machine": {"reco": "Decrease the time spent washing per load", "savetime": "", "saveamt": "", "savewatt": "", "saveprice": ""}}), recommendations