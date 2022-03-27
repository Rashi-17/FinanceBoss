import pandas as pd
import csv
from website.domains.classify_model import convert_categorical,train_model




def domain_classify():
    classifier = train_model()
    categorical_cols=['detail']
    dataframe_raw1 = pd.read_csv("user_expense.csv")
    final_df1 = convert_categorical(dataframe_raw1,categorical_cols)
    preds1 = classifier.predict(final_df1)
    

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
    
    return calulation,total

    
