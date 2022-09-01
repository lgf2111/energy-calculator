from webapp import db
from datetime import datetime


class Appliance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    watts = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)

    def __repr__(self):
        return f"Appliance('{self.name}', '{self.watts}', '{self.date_added}')"

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    appliances = db.relationship('Appliance', backref='brand', lazy=True)
    
    def __repr__(self):
        return f"Brand('{self.name}', '{self.date_added}')"