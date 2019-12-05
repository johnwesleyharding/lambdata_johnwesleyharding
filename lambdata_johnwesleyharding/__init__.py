import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


"""


"""

def trainvalidtest(df, features, target):
        
    train, test = train_test_split(df)
    
    X_train, X_valid, y_train, y_valid = train_test_split(train[features], train[target])
    X_test = test[features]
    y_test = test[target]
    
    return X_train, X_valid, y_train, y_valid, X_test, y_test


"""


"""

def monthdayyear(dataframe, datefeature):
    
    def createmonth(date):
        return date[:2]
    
    dataframe['Month'] = dataframe[datefeature].apply(createmonth)
    
    def createday(date):
        return date[3:5]
    
    dataframe['Day'] = dataframe[datefeature].apply(createday)
    
    def createyear(date):
        return date[6:]
    
    dataframe['Year'] = dataframe[datefeature].apply(createyear)
    
    return dataframe