from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class calculatorForm(FlaskForm):
    appliance = SelectField('Appliance', choices=[('Washing Machine', 'Refrigerator', 'Television', 'Air-conditioning')])
    brand = SelectField('Brand Name', choices=[('Panasonic', 'Samsung', 'Mitsubishi', 'Daikin', 'LG',  'Philips', 'Hitachi', )])
    ticks = SelectField('Efficiency Level', choices=[(1, 2, 3, 4, 5)])
    time_used = SelectField('Duration Used', choices=[('Less than 1h', '2h', '3h', 'More than 3h')])