from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required
from flask_login import login_required, current_user
from datetime import datetime
from website.models import Expense
#from .models import Expense
from . import db
import json

exp_view = Blueprint('exp_view',__name__)

@exp_view.route('/expenses', methods=['GET','POST'])
@login_required
def expenses():
    if request.form.get('display'):
        flash('Displaying!', category='success')
        display = Expense.query.filter_by(user_id=current_user.id)
        show=True
        return render_template('expenses.html',user=current_user,display=display,show=show)
    elif request.method == 'POST':
        date_ = request.form.get('date')
        detail = request.form.get('detail')
        amount = request.form.get('amount')
    
        if len(date_) < 1:
            flash('detail is too short!', category='error')
        elif len(detail)<1:
            flash('date is not selected!', category='error')
        elif len(amount)<1:
            flash('amount is too short!', category='error')
        else:
            date = datetime.strptime(date_, '%Y-%m-%dT%H:%M:%S')
            new_exp = Expense(date=date,details=detail, amount=amount, user_id=current_user.id)
            db.session.add(new_exp)
            db.session.commit()
            #exp = Expense.query.filter_by(details='food')
            flash('Expense added!', category='success')
            

    return render_template("expenses.html", user=current_user)