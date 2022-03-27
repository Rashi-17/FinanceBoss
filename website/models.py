from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(1000), nullable=False)
    savings = db.Column(db.Integer, default=3)
    saving_amount = db.Column(db.Integer, nullable=False)
    tenure_expected = db.Column(db.String(100))
    tenure_actual = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    user_name = db.Column(db.String(150), nullable=False)
    salary = db.Column(db.Integer)
    loggedin_date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    expenses = db.relationship('Expense')
    goals = db.relationship('Goal')
    domainPer = db.relationship('DomainPer')

class DomainPer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eating_out =  db.Column(db.Float, default=8)
    groceries =  db.Column(db.Float, default=9)
    clothes =  db.Column(db.Float, default=5)
    bills_and_rent =  db.Column(db.Float, default=15)
    housing =  db.Column(db.Float, default=7)
    stationary =  db.Column(db.Float, default=3)
    travel =  db.Column(db.Float, default=10)
    entertainment =  db.Column(db.Float,default=5)
    health =  db.Column(db.Float, default=9)
    sport =  db.Column(db.Float, default=5)
    others =  db.Column(db.Float, default=12)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

