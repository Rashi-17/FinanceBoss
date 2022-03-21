
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MinMaxScaler
#from sklearn.svm import SVC
#import csv


def normalize(df):
    # create a scaler object
    scaler = MinMaxScaler()
    # fit and transform the data
    df_norm = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    return df_norm

"""def dataframe_to_arrays(dataframe, categorical_cols, input_cols, output_cols=None):
    # Make a copy of the original dataframe
    dataframe1 = dataframe.copy(deep=True)
    # Convert non-numeric categorical columns to numbers
    for col in categorical_cols:
        dataframe1[col] = dataframe1[col].astype('category').cat.codes
    # Extract input & outupts as numpy arrays
    inputs_array = dataframe1[input_cols].to_numpy()
    if output_cols!=None:
        targets_array = dataframe1[output_cols].to_numpy()
        data_numpy = np.concatenate((inputs_array,targets_array),axis=1)
        return data_numpy
    return input_cols"""

def convert_categorical(dataframe, categorical_cols):
    # Make a copy of the original dataframe
    dataframe1 = dataframe.copy(deep=True)
    # Convert non-numeric categorical columns to numbers
    for col in categorical_cols:
        dataframe1[col] = dataframe1[col].astype('category').cat.codes
    return dataframe1
def train_model():
    dataframe_raw = pd.read_csv("NEWDataset.csv")
    #input_cols=['detail','amount']
    #output_cols=['domain']
    categorical_cols=['detail']
    final_df = convert_categorical(dataframe_raw,categorical_cols)#pd.DataFrame(data_numpy,columns=['detail','amount','domain'])
    norm_df = normalize(final_df.drop('domain',axis=1))
    X_train, X_test, y_train, y_test = train_test_split(norm_df,final_df['domain'],random_state=29, shuffle=True,test_size=0.25)
    clf = OneVsRestClassifier(RandomForestClassifier(max_depth=4,random_state=0)).fit(X_train,y_train)
    preds = clf.predict(X_test)
    #print(preds)
    #print(X_test)
    sc = clf.score(X_test,y_test)
    print(sc)
    return clf
"""train_model()
    
d = pd.read_csv("NEWDataset.csv")
tr,te,y_tr,y_te=train_test_split(d.drop('domain',axis=1),d['domain'],random_state=29, shuffle=True,test_size=0.25)
for t in range(len(te)):
    print(d.loc[t,:])
    print("\n")
print(len(te))"""
#model()
"""#dataframe_raw['domain'].replace({'Eating Out':1, 'Groceries':2, 'Clothes':3, 'Bills and Rent':4, 'Housing':5, 
 #                       'Stationary':6, 'Travel':7, 'Entertainment':8, 'Health':9, 'Sport':10, 'Others':11},inplace=True)
dom = ['Eating Out','Groceries','Clothes','Bills and Rent','Housing','Stationary','Travel','Entertainment','Health','Sport','Others']
le = preprocessing.LabelEncoder()
le.fit(dom)
le.transform(dataframe_raw['domain'])
print(dataframe_raw.head())"""



#data_numpy = dataframe_to_arrays(dataframe_raw,categorical_cols,input_cols,output_cols)
"""final_df = convert_categorical(dataframe_raw,categorical_cols).drop('date',axis=1)#pd.DataFrame(data_numpy,columns=['detail','amount','domain'])
norm_df = normalize(final_df.drop('domain',axis=1))
X_train, X_test, y_train, y_test = train_test_split(norm_df,final_df['domain'],random_state=29, shuffle=True,test_size=0.25)"""
#print(dataframe_raw.sample(n=50))
"""myModel = LogisticRegression(max_iter=300, solver='newton-cg',multi_class='multinomial')
myModel.fit(X_train.to_numpy().reshape(-1,1),y_train)
preds = myModel.predict(X_test.to_numpy().reshape(-1,1))
#print(X_test)
print(preds)
print(y_test)
score = myModel.score(X_test.to_numpy().reshape(-1,1),y_test)
print(score)"""

"""clf = OneVsRestClassifier(SVC()).fit(X_train,y_train)
preds = clf.predict(X_test)
print(preds)
print(y_test)
sc = clf.score(X_test,y_test)
print(sc)"""


#print(dataframe_raw)

#plt.plot(X_train.to_numpy(),y_train.to_numpy(),'o')
#plt.show()
"""dataframe_raw1 = pd.read_csv("user_expense.csv")
final_df1 = convert_categorical(dataframe_raw1,categorical_cols)#pd.DataFrame(data_numpy,columns=['detail','amount','domain'])
norm_df1 = normalize(final_df1)
preds1 = clf.predict(norm_df1)
print(norm_df1)
print(final_df1)
print(preds1)

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
        i+=1"""



