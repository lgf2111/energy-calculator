from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = '13050e1c636532b3237d222fcd7fd944'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializations
db = SQLAlchemy(app)
admin = Admin(app, name='Energy Calculator', template_mode='bootstrap4')
from webapp.models import Brand, Appliance
admin.add_view(ModelView(Appliance, db.session))
admin.add_view(ModelView(Brand, db.session))
class LogoutView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('home'))
admin.add_view(LogoutView(name='Logout', endpoint='Logout'))

from webapp import routes
