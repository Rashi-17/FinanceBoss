from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import DomainPer, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
               # flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login_signup.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/update', methods=['GET','POST'])
def update():
    #flash('Salary updated!56576567', category='success')
    if request.method == 'POST':
        if request.form.get('updateSal'):
            salary = request.form.get('salary')
        
            if len(salary) < 1:
                    flash('Salary is too short!', category='error')
            else:
                salary = request.form.get('salary')
                db.session.query(User).filter(User.id == current_user.id).update({User.salary:salary})
                db.session.commit()
                flash('Salary updated!', category='success')
                #return redirect(url_for('views.home'))
        if request.form.get('domain') :
            if request.form.get('amount').lower()=='yes':
                return redirect(url_for('auth.domainPer'))
            else:
                return redirect(url_for('views.home'))
       # flash(' updated!1223', category='success')
   # flash('Salary updated!567', category='success')
    return render_template("update.html",user=current_user)

@auth.route('/domainPer', methods=['Get','POST'])
def domainPer():
    if request.method == 'POST':
        eating_out =  request.form.get('eating out')
        groceries =  request.form.get('groceries')
        clothes =  request.form.get('clothes')
        bills_and_rent =  request.form.get('bills')
        housing =  request.form.get('housing')
        stationary =  request.form.get('stationary')
        travel = request.form.get('travel')
        entertainment =  request.form.get('entertainment')
        health =  request.form.get('health')
        sport =  request.form.get('sport')
        others =  request.form.get('others')
        if len(eating_out) < 1 or len(groceries)<1 or len(clothes)<1 or len(bills_and_rent)<1 or len(housing)<1 or len(stationary)<1 or len(travel)<1 or len(entertainment)<1 or len(health)<1 or len(sport)<1 or len(others)<1:
            flash('Please enter all the fields!', category='error')
        else:
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.eating_out:eating_out})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.groceries:groceries})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.clothes:clothes})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.bills_and_rent:bills_and_rent})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.housing:housing})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.stationary:stationary})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.travel:travel})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.entertainment:entertainment})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.health:health})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.sport:sport})
            db.session.query(DomainPer).filter(DomainPer.user_id == current_user.id).update({DomainPer.others:others})
            db.session.commit()
            #flash('!', category='error')
            return redirect(url_for('views.home'))
    
    return render_template('domain.html',user=current_user)

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        User.query.filter(User.email.endswith('@example.com')).all()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, user_name=name, password=generate_password_hash(
                password1, method='sha256'), loggedin_date=datetime.now())
            db.session.add(new_user)
            user = User.query.filter_by(email=email).first()
            domain = DomainPer(user_id = user.id)
            db.session.add(domain)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('auth.update')) 

    return render_template("login_signup.html", user=current_user)