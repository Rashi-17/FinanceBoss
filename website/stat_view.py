from distutils.log import error
from flask import Blueprint, render_template, flash, request
from flask_login import login_required
from flask_login import login_required, current_user
from datetime import datetime, timedelta
from website.models import DomainPer, Expense, User
from website.domains.domain_classify import domain_classify
from . import db
import csv
from plotly import utils
import plotly.graph_objs as go
import json

import plotly.graph_objects as px

stat_view = Blueprint('stat_view',__name__)

def expected_expenses(id,salary):
    expect_exp={'Eating Out':0, 'Groceries':0, 'Clothes':0, 'Bills and Rent':0, 'Housing':0, 
                       'Stationary':0, 'Travel':0, 'Entertainment':0, 'Health':0, 'Sport':0, 'Others':0}
            
    dom_user = DomainPer.query.filter_by(user_id = id)

    for d in dom_user:
        expect_exp['Eating Out']=(salary*d.eating_out)/100
        expect_exp['Groceries']=(salary*d.groceries)/100
        expect_exp['Clothes']=(salary*d.clothes)/100
        expect_exp['Bills and Rent']=(salary*d.bills_and_rent)/100
        expect_exp['Housing']=(salary*d.housing)/100
        expect_exp['Stationary']=(salary*d.stationary)/100
        expect_exp['Travel']=(salary*d.travel)/100
        expect_exp['Entertainment']=(salary*d.entertainment)/100
        expect_exp['Health']=(salary*d.health)/100
        expect_exp['Sport']=(salary*d.sport)/100
        expect_exp['Others']=(salary*d.others)/100
    return expect_exp


@stat_view.route('/statistics', methods=['GET','POST'])
@login_required
def statistics():
    user = User.query.filter_by(id = current_user.id)
    for u in user:
        id = u.id
        salary = u.salary
    if request.method=='POST' and request.form.get('stats') == 'till_date':
        record = db.session.query(Expense).filter(Expense.user_id == id, Expense.date<=datetime.now())
        s = round(salary/30)
        date=[]
        for r in record:
            date.append(r.date)
        min_date = min(date)
        days = datetime.now() - min_date
        salary = days.days * s
            
        if record:
            create_csv(record)
            domains,total = domain_classify()
            domain_name = list(domains.keys())
            domain_total = list(domains.values())
            
            
            trace1 = go.Bar(x=domain_name, y=domain_total)
            layout = go.Layout(title="Expenses of domain", xaxis=dict(title="Domain"),
                            yaxis=dict(title="Expense"), )
            data = [trace1]
            plot = go.Figure(data=data, layout=layout)
            fig_json = json.dumps(plot, cls=utils.PlotlyJSONEncoder)
        else:
            flash("No expense is added...Please add some of your expenditures...",category=error)
            return render_template("statistics.html", user=current_user,show=False)

    else:
        filter_after = datetime.today() - timedelta(days = 30)
        record_30 = Expense.query.filter(Expense.date >= filter_after, Expense.user_id==id).all()
        
                
        if record_30:
            create_csv(record_30)
            expect_exp = expected_expenses(current_user.id,salary)
            expected_domain_total = list(expect_exp.values())
           
            domains,total = domain_classify()
            domain_name = list(domains.keys())
            domain_total = list(domains.values())
            
            trace1 = go.Bar(x=domain_name, y=domain_total)
            layout = go.Layout(title="Expenses of domain", xaxis=dict(title="Domain"),
                            yaxis=dict(title="Expense"), )
            data = [trace1]
            plot = px.Figure(data=[go.Bar(
            name = 'Actual expense',
            x = domain_name,
            y = domain_total
        ),
                            go.Bar(
            name = 'Desire Expense',
            x = domain_name,
            y = expected_domain_total 
        )
        ],layout=layout)
            fig_json = json.dumps(plot, cls=utils.PlotlyJSONEncoder)
            
        else:
            flash("No expense is added for 30 days before...Please add some of your expenditures...",category="error")
            return render_template("statistics.html", user=current_user,show=False)      

    return render_template("statistics.html", user=current_user, plot=fig_json, salary=salary, total=total,show=True)

    
def create_csv(record):
    with open('user_expense.csv', 'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date','detail','amount'])
        for r in record:
            rec=[]
            rec.append(r.date.day)
            rec.append(r.details)
            rec.append(r.amount)
            writer.writerow(rec)
