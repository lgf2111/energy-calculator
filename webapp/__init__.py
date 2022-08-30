from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = '13050e1c636532b3237d222fcd7fd944'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializations
db = SQLAlchemy(app)
admin = Admin(app, name='Energy Calculator', template_mode='bootstrap4')

from webapp import routes
