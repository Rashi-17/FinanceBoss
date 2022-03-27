from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required
from flask_login import login_required, current_user
from . import db
from website.models import Goal
from datetime import datetime
from website.stat_view import expected_expenses, create_csv
from website.models import Expense, User
from datetime import datetime, timedelta
from website.domains.domain_classify import domain_classify
import json

per_goals_view = Blueprint('per_goals_view',__name__)

def months_to_achieve(savings, amount):
    months=0
    while(amount>=0):
        amount-=savings
        months+=1
    return months

@per_goals_view.route('/per_goals', methods=['GET','POST'])
@login_required
def per_goals():
    
    if request.form.get('display'):
        flash('Displaying!', category='success')
        display = Goal.query.filter_by(user_id=current_user.id)
        show=True
        user = User.query.filter_by(id = current_user.id)
        for u in user:
            id = u.id
            salary = u.salary
        filter_after = datetime.today() - timedelta(days = 30)
        record_30 = Expense.query.filter(Expense.date >= filter_after, Expense.user_id==id).all()
        create_csv(record_30)
        _,total = domain_classify()
        saved_30 = salary - total
        for g in display:
            savings = g.savings
            save_amount = g.saving_amount
            expect_mon = months_to_achieve(savings,save_amount)
            actual_mon = months_to_achieve(saved_30,save_amount)
            db.session.query(Goal).filter(Goal.user_id == current_user.id, Goal.id == g.id).update({Goal.tenure_expected:expect_mon})
            db.session.query(Goal).filter(Goal.user_id == current_user.id, Goal.id == g.id).update({Goal.tenure_actual:actual_mon})
            db.session.commit()



        return render_template('per_goals.html',user=current_user,display=display,show=show)
    elif request.method == 'POST':
        goal = request.form.get('Goal')
        amt = request.form.get('Amount')
        saving = request.form.get('Saving')

        if len(goal) < 1:
            flash('Goal detail is too short!', category='error')
        elif len(amt)<1:
            flash('amount is too short!', category='error')
        else:
            user = User.query.filter_by(id = current_user.id)
            for u in user:
                id = u.id
                salary = u.salary
            if len(saving)<1:
                save = salary*0.12
            else:
                save = (salary*int(saving))/100
            new_goal = Goal(savings=save,details=goal, saving_amount=amt, user_id=id)
            db.session.add(new_goal)
            db.session.commit()
            flash('Goal added!', category='success')
        

            
    return render_template('per_goals.html',user=current_user)

@per_goals_view.route('/delete-goal', methods=['POST'])
def delete_note():
    goal = json.loads(request.data)
    goalId = goal['goalId']
    goal = Goal.query.get(goalId)
    if goal:
        if goal.user_id == current_user.id:
            db.session.delete(goal)
            db.session.commit()

    return jsonify({})