from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    identity = db.Column(db.String(10))
    company = db.Column(db.String(100))

class Voucher(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    company = db.Column(db.String(100))
    denomination = db.Column(db.Integer)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

class LoyaltyPoints(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    points = db.Column(db.Integer)

class User_Voucher(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100))
    #voucher_id = db.Column(db.String(100))  ## Didn't have time to integrate this
    company = db.Column(db.String(100))
    voucher = db.Column(db.String(100)) # Name of Voucher
    denomination = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    company = db.Column(db.String(100))
    denomination = db.Column(db.Integer)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)