from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from flask_login import login_required, current_user
from .models import User
from . import db


views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.form.get('add_exp'):
        #flash('added exp!', category='success')
        return redirect(url_for('exp_view.expenses'))
    elif request.form.get('stats'):
        #flash('showing stats!', category='success')
        return redirect(url_for('stat_view.statistics'))
    elif request.form.get('per_goal'):
        #flash('showing stats!', category='success')
        return redirect(url_for('per_goals_view.per_goals'))
    elif request.form.get('advice'):
        #flash('showing stats!', category='success')
        return redirect(url_for('advice_view.advice'))
    """elif request.method == 'POST':
        salary = request.form.get('salary')
    
        if len(salary) < 1:
                flash('Salary is too short!', category='error')
        else:
            salary = request.form.get('salary')
            db.session.query(User).filter(User.id == current_user.id).update({User.salary:salary})
            db.session.commit()
            flash('Salary updated!', category='success')"""
    

    return render_template("home.html", user=current_user)
