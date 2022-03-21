from flask import Blueprint, render_template, flash, request
from flask_login import login_required
from flask_login import login_required, current_user
from sqlalchemy import true
from . import db
from website.models import Goal
from datetime import datetime

per_goals_view = Blueprint('per_goals_view',__name__)

@per_goals_view.route('/per_goals', methods=['GET','POST'])
@login_required
def per_goals():
    #flash('goals added!', category='success')
    if request.form.get('display'):
        flash('Displaying!', category='success')
        display = Goal.query.filter_by(user_id=current_user.id)
        show=True
        return render_template('per_goals.html',user=current_user,display=display,show=show)
    elif request.method == 'POST':
        goal = request.form.get('Goal')
        amt = request.form.get('Amount')
        tenure = request.form.get('Tenure')

        if len(goal) < 1:
            flash('Goal detail is too short!', category='error')
        elif len(amt)<1:
            flash('amount is too short!', category='error')
            
        elif len(tenure)<1:
            flash('date is not selected!', category='error')
        else:
            date = datetime.strptime(tenure, '%Y-%m-%dT%H:%M:%S')
            new_goal = Goal(target_date=date,details=goal, saving_amount=amt, user_id=current_user.id)
            db.session.add(new_goal)
            db.session.commit()
            #exp = Expense.query.filter_by(details='food')
            flash('Goal added!', category='success')
    
            
    return render_template('per_goals.html',user=current_user)
