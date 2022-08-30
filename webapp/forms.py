import enum
from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, IntegerField
from wtforms.validators import DataRequired
from webapp.models import Appliance, Brand

class CalculatorForm(FlaskForm):
    appliance_list = sorted([(_, _) for _ in set([_.name for _ in Appliance.query.all()])])
    brand_list = sorted([(_.name, _.name) for _ in Brand.query.all()])
    brand_list.append(brand_list.pop(brand_list.index(("Others", "Others")))) # Shift Others to last element
    ticks_list = [(_, _) for _ in range(1,6)]
   
    appliance = SelectField('Appliance', choices=appliance_list, validators=[DataRequired()])
    brand = SelectField('Brand Name', choices=brand_list, validators=[DataRequired()])
    ticks = RadioField('Efficiency Level', choices=ticks_list, validators=[DataRequired()])
    usage = IntegerField('Duration Used',  validators=[DataRequired()])