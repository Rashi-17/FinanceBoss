from flask import Blueprint, render_template
from flask_login import login_required
from flask_login import login_required, current_user
from website.stat_view import expected_expenses, create_csv
from website.models import Expense, User
from datetime import datetime, timedelta
from website.domains.domain_classify import domain_classify

advice_view = Blueprint('advice_view',__name__)

@advice_view.route('/advice', methods=['GET','POST'])
@login_required
def advice():
    
    user = User.query.filter_by(id = current_user.id)
    for u in user:
        id = u.id
        salary = u.salary
    expect_exp = expected_expenses(id,salary)
    filter_after = datetime.today() - timedelta(days = 30)
    record_30 = Expense.query.filter(Expense.date >= filter_after, Expense.user_id==id).all()
    create_csv(record_30)
    domains,_ = domain_classify()
    msg=""
    exceed=False
    
    if(expect_exp['Eating Out']<domains['Eating Out']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in EATING OUT. \nYou should reduced your expenditures in EATING FOOD OUT..."
    if(expect_exp['Groceries']<domains['Groceries']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in GROCERIES. \nYou should reduced your expenditures in GROCERIES..."
    if(expect_exp['Clothes']<domains['Clothes']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in CLOTHES. \nYou should reduced your expenditures in CLOTHES..."
    if(expect_exp['Bills and Rent']<domains['Bills and Rent']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in BILLS AND RENTS. \nYou should reduced your expenditures in BILLS AND RENTS..."
    if(expect_exp['Housing']<domains['Housing']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in HOUSING. \nYou should reduced your expenditures in BILLS AND RENTS..."
    if(expect_exp['Stationary']<domains['Stationary']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in STATIONARY. \nYou should reduced your expenditures in STATIONARY..."
    if(expect_exp['Travel']<domains['Travel']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in TRAVEL. \nYou should reduced your expenditures in TRAVEL..."
    if(expect_exp['Entertainment']<domains['Entertainment']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in ENTERTAINMENT. \nYou should reduced your expenditures in ENTERTAINMENT..."
    if(expect_exp['Health']<domains['Health']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in HEALTH. \nYou should reduced your expenditures in HEALTH..."
    if(expect_exp['Sport']<domains['Sport']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in SPORTS. \nYou should reduced your expenditures in SPORTS..."
    if(expect_exp['Others']<domains['Others']):
        exceed=True
        msg+="\n\nYou are excceeding the limit that you set for spendings in OTHERS SECTION. \nYou should reduced your expenditures in OTHERS SECTION... "
    if not exceed:
        msg="You spending in each domainis upto the limits that you set. \nGood going... "
            
    return render_template('advice.html',user=current_user,msg=msg,exceed=exceed)
