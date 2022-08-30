import enum
from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, IntegerField
from wtforms.validators import DataRequired
from webapp.models import Appliance, Brand

class CalculatorForm(FlaskForm):
    appliance_list = [(_.name, _.name) for _ in Appliance.query.all()]
    brand_list = [(_.name, _.name) for _ in Brand.query.all()]
    ticks_list = [(_, _) for _ in range(1,6)]
   

    appliance = SelectField('Appliance', choices=appliance_list, validators=[DataRequired()])
    brand = SelectField('Brand Name', choices=brand_list, validators=[DataRequired()])
    ticks = RadioField('Efficiency Level', choices=ticks_list, validators=[DataRequired()])
    usage = IntegerField('Duration Used',  validators=[DataRequired()])