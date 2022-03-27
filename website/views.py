from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from flask_login import login_required, current_user



views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.form.get('add_exp'):
        return redirect(url_for('exp_view.expenses'))
    elif request.form.get('stats'):
        return redirect(url_for('stat_view.statistics'))
    elif request.form.get('per_goal'):
        return redirect(url_for('per_goals_view.per_goals'))
    elif request.form.get('advice'):
        return redirect(url_for('advice_view.advice'))

    return render_template("home.html", user=current_user)
