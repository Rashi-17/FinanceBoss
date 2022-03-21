from email.policy import default
from . import db #import db from website
from flask_login import UserMixin
from sqlalchemy.sql import func

"""
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))# in sql user"""

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(1000), nullable=False)
    target_date = db.Column(db.Date(), nullable=False)
    saving_amount = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    user_name = db.Column(db.String(150), nullable=False)
    salary = db.Column(db.Integer)
    loggedin_date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    #notes = db.relationship('Note')
    expenses = db.relationship('Expense')
    goals = db.relationship('Goal')
    domainPer = db.relationship('DomainPer')

class DomainPer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eating_out =  db.Column(db.Float, default=10)
    groceries =  db.Column(db.Float, default=10)
    clothes =  db.Column(db.Float, default=5)
    bills_and_rent =  db.Column(db.Float, default=25)
    housing =  db.Column(db.Float, default=8)
    stationary =  db.Column(db.Float, default = 5)
    travel =  db.Column(db.Float, default=15)
    entertainment =  db.Column(db.Float,default=5)
    health =  db.Column(db.Float, default=10)
    sport =  db.Column(db.Float, default=5)
    others =  db.Column(db.Float, default=12)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

