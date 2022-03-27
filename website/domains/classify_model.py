
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier



def convert_categorical(dataframe, categorical_cols):
    # Make a copy of the original dataframe
    dataframe1 = dataframe.copy(deep=True)
    # Convert non-numeric categorical columns to numbers
    for col in categorical_cols:
        dataframe1[col] = dataframe1[col].astype('category').cat.codes
    return dataframe1
def train_model():
    dataframe_raw = pd.read_csv("NEWDataset.csv")
    categorical_cols=['detail']
    final_df = convert_categorical(dataframe_raw,categorical_cols)
    X_train, X_test, y_train, y_test = train_test_split(final_df.drop('domain',axis=1),final_df['domain'],random_state=29, shuffle=True,test_size=0.25)
    clf = OneVsRestClassifier(RandomForestClassifier(max_depth=4,random_state=0)).fit(X_train,y_train)
    sc = clf.score(X_test,y_test)
    print(sc)
    return clf
