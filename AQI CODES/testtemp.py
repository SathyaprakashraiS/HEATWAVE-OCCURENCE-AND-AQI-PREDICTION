# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 18:36:10 2023

@author: SATHYA
"""

# Import required libraries
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense, Dropout
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.optimizers import Adam

# Define the input sequence

df=pd.read_excel("D:/SEM VIII/MINI PROJECT/PRE PROCESSOR/PROCESSED WEATHER DATA/WARANGAL_ELKATHURTHI_ALL.xlsx",parse_dates=['date'],index_col='date')
df_train = df["temp_max"]

df_as_np = df.to_numpy()
seq = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#seq=df_as_np

# Define the number of time steps
n_steps = 3

# Split the sequence into samples
X, y = [], []

def df_to_X_y(df,window_size):
    print("over here 0")
    try:
        print("trying")
        df_as_np = df.to_numpy()
        print("sucessful")
    except:
        print("in except")
        df_as_np=df
        print("ended except")
    print("inga eruken")
    print("ASd",len(df_as_np))
    X = []
    y = []
    for i in range(len(df_as_np)-window_size):
        row = [[a] for a in df_as_np[i:i+window_size]]
        X.append(row)
        label = df_as_np[i+window_size]
        y.append(label)
    return np.array(X).astype('float32'),np.array(y).astype('float32')

'''
for i in range(len(seq)):
    end_ix = i + n_steps
    if end_ix > len(seq) - 1:
        break
    seq_x, seq_y = seq[i:end_ix], seq[end_ix]
    X.append(seq_x)
    y.append(seq_y)

# Reshape the input samples
X = np.array(X).reshape((len(X), n_steps, 1))
'''

X,y=df_to_X_y(seq,3)

# Define the LSTM model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_steps, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Fit the model to the data
model.fit(X, y, epochs=200, verbose=0)

# Use the model to make predictions
x_input = np.array([7, 8, 9]).reshape((1, n_steps, 1))
yhat = model.predict(x_input, verbose=0)

# Predict 30 future values
for i in range(30):
    x_input = np.append(x_input[:,1:,:], yhat)
    yhat = model.predict(x_input, verbose=0)
    print(yhat)
