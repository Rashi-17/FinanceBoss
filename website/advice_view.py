from flask import Blueprint, render_template, flash
from flask_login import login_required
from flask_login import login_required, current_user

advice_view = Blueprint('advice_view',__name__)

@advice_view.route('/advice', methods=['GET','POST'])
@login_required
def advice():
    #flash('advice added!', category='success')
            
    return render_template('advice.html',user=current_user)
