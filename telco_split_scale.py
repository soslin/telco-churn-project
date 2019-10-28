import pandas as pd
from env import host, user, password

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
import wrangle_telco
from sklearn.preprocessing import StandardScaler


df_t = wrangle_telco.wrangle_telco()
X = df_t.drop(columns=['churn', 'customer_id', 'internet_service_type', 'contract_type', 'payment_type'])
y = pd.DataFrame(df_t['churn'])

#1. split_my_data(X, y)
def split_my_data(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .7, random_state = 123)
    return X_train, X_test, y_train, y_test

#X_train, X_test, y_train, y_test = split_my_data(X,y)



def standard_scaler(X_train, X_test):
    scaler_x_train = StandardScaler(copy=True, with_mean=True, with_std=True)\
                .fit(X_train)
    scaler_x_test = StandardScaler(copy=True, with_mean=True, with_std=True)\
                .fit(X_test)
    train_x_scaled_data = pd.DataFrame(scaler_x_train.transform(X_train), columns = X_train.columns.values).set_index([X_train.index.values])
    
    test_x_scaled_data = pd.DataFrame(scaler_x_test.transform(X_test), columns = X_test.columns.values).set_index([X_test.index.values])
    
    return train_x_scaled_data, test_x_scaled_data, scaler_x_train, scaler_x_test
    
#train_x_scaled_data, test_x_scaled_data,scaler_x_train, scaler_x_test = standard_scaler(X_train,X_test)


