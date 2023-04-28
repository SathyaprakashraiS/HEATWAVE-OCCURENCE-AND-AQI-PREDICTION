# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:26:30 2023

@author: SATHYA
"""

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

#df = pd.read_excel("D:/SEM VIII/MINI PROJECT/PRE PROCESSOR/2018/ADILABAD/Adilabad_Bela_2018.xlsx")
df=pd.read_excel("D:/SEM VIII/MINI PROJECT/CNN/all.xlsx",parse_dates=['date'],index_col='date')

df.head(30)
columns = ["District","mandal","rainfall","min_temp","max_temp","min_hum","max_hum","min_speed","max_speed"]

df.columns = columns
#df.index = pd.to_datetime(df['date'], format='%d-%m-%Y')
df[:26]

# train_dates = pd.to_datetime(df['date'],infer_datetime_format=True)
# print(train_dates.tail(15)) #Check last few dates. 

cols = list(df)[5:10]
print(cols)

# df_train = df.drop(["District","mandal","date"],axis="columns")
df_train = df["max_temp"]

def df_to_X_y(df,window_size=5):
    try:
        df_as_np = df.to_numpy()
    except:
        df_as_np=df
    print(len(df_as_np))
    X = []
    y = []
    for i in range(len(df_as_np)-window_size):
        row = [[a] for a in df_as_np[i:i+window_size]]
        X.append(row)
        label = df_as_np[i+5]
        y.append(label)
    return np.array(X).astype('float32'),np.array(y).astype('float32')
    
WINDOW_SIZE = 5
# print(df.tail(30))
X,y = df_to_X_y(df_train,WINDOW_SIZE)
print(X.shape,y.shape)


X_train, y_train = X[:-250], y[:-250]
# X_val1, y_val1 = X1[60000:65000], y1[60000:65000]
X_test, y_test = X[-250:], y[-250:]
# X_train1.shape, y_train1.shape, X_val1.shape, y_val1.shape, X_test1.shape, y_test1.shape



model = Sequential()
model.add(InputLayer((5, 1)))
model.add(LSTM(64,))
model.add(Dense(8, 'relu'))
model.add(Dense(1, 'linear'))

model.summary()

cp1 = ModelCheckpoint('testmodel1/', save_best_only=True)
model.compile(loss=MeanSquaredError(), optimizer=Adam(learning_rate=0.01), metrics=[RootMeanSquaredError()])
model.fit(X_train, y_train, validation_split=0.2, epochs=300,callbacks = [cp1])

from tensorflow.keras.models import load_model
model1 = load_model('testmodel1/')

#new_df = df.drop(["month"],axis=1)
#from neuralprophet import NeuralProphet
#m=NeuralProphet
#new_df= df.drop(["District","mandal","rainfall","min_temp","min_hum","max_hum","min_speed","max_speed"],axis=1)

#forecast = model.predict(future)

train_predictions = model.predict(X_train).flatten()
train_results = pd.DataFrame(data={'Train Predictions':train_predictions, 'Actuals':y_train})
print(train_results)
plt.plot(train_predictions, label='train')
plt.plot(y_train, label='test')
plt.legend()
plt.show()


#actual test
test_predictions = model.predict(X_test).flatten()
test_results = pd.DataFrame(data={'Test Predictions':test_predictions, 'Actuals':y_test})
print(test_results)
plt.plot(test_predictions, label='train')
plt.plot(y_test, label='test')
plt.legend()
plt.show()

print(test_predictions[-1])
#predictions=test_predictions
predictions=test_predictions
data=test_predictions
future=[]
for i in range(len(data)):
    future.append(data[i])
#predictions,tpred=df_to_X_y(df_train,WINDOW_SIZE)
'''
for i in range(10):
    print("i is",i)
    print("length is: ",len(predictions))
    Xx,yy = df_to_X_y(predictions,WINDOW_SIZE)
    new=model.predict(Xx).flatten()
    predictions=new
    print(new[-1])
    future.append(new[-1])
'''
i=0
print("length of future is: ",len(future))

'''
while(True):
    try:
        print("i is",i)
        print("length is: ",len(predictions))
        print("length of future is: ",len(future))
        Xx,yy = df_to_X_y(predictions,WINDOW_SIZE)
        new=model.predict(Xx).flatten()
        predictions=new
        print(new[-1])
        future.append(new[-1])
        i+=1
    except:
        break
    '''

for i in range(364):
    try:
        print("i is",i)
        print("length is: ",len(predictions))
        print("length of future is: ",len(future))
        Xx,yy = df_to_X_y(df_train,WINDOW_SIZE)
        new=model.predict(Xx).flatten()
        predictions=new
        print("predicted value is ",new[-1])
        future.append(new[-1])
        #temp=pd.DataFrame({"max_temp":[new[-1]]})
        temp=pd.Series([new[-1]])
        df_train=df_train.append(temp)
        #i+=1
    except:
        break

'''
#df2 = pd.DataFrame({"a":[1]})
df2 = pd.DataFrame({"max_temp":[1]})
  
# for appending df2 at the end of df1
#df1 = df1.append(df2, ignore_index = True)
z=df
z=z.append(df2)
'''