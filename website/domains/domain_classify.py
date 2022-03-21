#from website import convert_categorical
import pandas as pd
import csv
from plotly import utils
from website.domains.classify_model import convert_categorical,normalize,train_model

"""import plotly.graph_objs as go
import json
import plotly.offline as plt"""


def domain_classify():
    classifier = train_model()
    categorical_cols=['detail']
    dataframe_raw1 = pd.read_csv("user_expense.csv")
    final_df1 = convert_categorical(dataframe_raw1,categorical_cols)#pd.DataFrame(data_numpy,columns=['detail','amount','domain'])
    norm_df1 = normalize(final_df1)
    preds1 = classifier.predict(norm_df1)
    """print(norm_df1)
    print(final_df1)
    print(preds1)"""

    with open('user_expense.csv','r') as read_obj,\
        open('with_domain.csv','w',newline='') as write_obj:
        read = csv.reader(read_obj)
        write = csv.writer(write_obj)
        write.writerow(['date','detail','amount','domain'])
        next(read)
        i=0
        for row in read:
            row.append(preds1[i])
            write.writerow(row) 
            i+=1

    calulation={'Eating Out':0, 'Groceries':0, 'Clothes':0, 'Bills and Rent':0, 'Housing':0, 
                       'Stationary':0, 'Travel':0, 'Entertainment':0, 'Health':0, 'Sport':0, 'Others':0}
    dataset = pd.read_csv("with_domain.csv")
    total = dataset['amount'].sum()
    for i in range(len(dataset)):
        if dataset.loc[i,'domain'] == 'Eating Out':
            calulation['Eating Out']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Groceries':
            calulation['Groceries']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Clothes':
            calulation['Clothes']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Bills and Rent':
            calulation['Bills and Rent']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Housing':
            calulation['Housing']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Stationary':
            calulation['Stationary']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Travel':
            calulation['Travel']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Entertainment':
            calulation['Entertainment']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Health':
            calulation['Health']+=dataset.loc[i,'amount']
        elif dataset.loc[i,'domain'] == 'Sport':
            calulation['Sport']+=dataset.loc[i,'amount']
        if dataset.loc[i,'domain'] == 'Others':
            calulation['Others']+=dataset.loc[i,'amount']
    """domain_name = list(calulation.keys())
    domain_total = list(calulation.values())
    
    trace1 = go.Bar(x=domain_name, y=domain_total)
    layout = go.Layout(title="Expenses of domain", xaxis=dict(title="Domain"),
                       yaxis=dict(title="Expense"), )
    data = [trace1]
    fig = go.Figure(data=data, layout=layout)
    fig_json = json.dumps(fig, cls=utils.PlotlyJSONEncoder)
    plt.plot(fig)"""
    #print(calulation)
    return calulation,total

    
