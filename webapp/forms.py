from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    appliance = SelectField('Appliance', choices=[('Washing Machine', 'Refrigerator', 'Television', 'Air-conditioning')], validators=[DataRequired()])
    brand = SelectField('Brand Name', choices=[('Panasonic', 'Samsung', 'Mitsubishi', 'Daikin', 'LG',  'Philips', 'Hitachi', )], validators=[DataRequired()])
    ticks = SelectField('Efficiency Level', choices=[(1, 2, 3, 4, 5)], validators=[DataRequired()])
    time_used = SelectField('Duration Used', choices=[('Less than 1h', '2h', '3h', 'More than 3h')], validators=[DataRequired()])