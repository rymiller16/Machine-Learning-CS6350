#Ryan Miller
#Machine Learning
#Assignment 5
#Question 3 - Logistic Regreession

import numpy as np 
import pandas as pd
import random
import matplotlib.pyplot as plt

path1 = 'bank-note/test.csv'
path2 = 'bank-note/train.csv'
test_df = pd.read_csv(path1,header=None)
train_df = pd.read_csv(path2,header=None)

test_df.insert(loc=0,column='4',value=1)     #setting bias
train_df.insert(loc=0,column='4',value=1)

X_train = (train_df.iloc[:,:-1]).values.tolist()
y_train_raw = (train_df.iloc[:,-1]).values.tolist()
dispatcher ={0:-1,1:1}
y_train = [dispatcher[lb] for lb in y_train_raw]
X_test = (test_df.iloc[:,:-1]).values.tolist()
y_test_raw = (test_df.iloc[:,-1]).values.tolist()
y_test = [dispatcher[lb] for lb in y_test_raw]

#Parameters
w = np.zeros(len(X_train[0]))
w = np.asmatrix(w)
g = 1
d = 0.001
var = [0.01,0.1,0.5,1,3,5,10,100]
sig = var[1]
num_epochs = 100

#MAP estimation 
w_map = np.random.normal(0,sig,len(X_train[0]))
w_map = np.asmatrix(w_map)
weights = [None]*num_epochs
norm = [None]*(num_epochs)

#ML estimation 
w_ml = np.zeros(len(X_train[0]))
w_ml = np.asmatrix(w_ml)

def Log_Regression(num_epochs,X_train,y_train,sig,g,w,d):
    for t in range(num_epochs):
        random.shuffle(X_train)
        for i in range(len(X_train)):
            g_t = (g)/(1+(g/d)*t)
            stuff = np.multiply(-i,(1-sig))
            w = w - g_t*(stuff*np.multiply(y_train[i],X_train[i]))
        weights[t] = w
        if t > 0:
            norm[t] = np.linalg.norm(weights[t]-weights[t-1])
    return w, weights, norm

def testing_error(w,X,y):
    err = 0
    for i in range(len(X)):
        pred = np.sign(np.matmul(w,np.transpose(np.asarray(X[i]))))
        if pred != y[i]:
            err = err+1
    return err/len(X)

#MAP
plt.figure(1)
w_map_r, weights_map_r, map_norm = Log_Regression(num_epochs,X_train,y_train,sig,g,w_map,d)
map_error_test = testing_error(w_map_r,X_test,y_test)
map_error_train = testing_error(w_map_r,X_train,y_train)
print(map_error_train)
print(map_error_test)
plt.plot(range(len(map_norm)),map_norm,color='red',label = 'Variance: %f' % (sig))
plt.xlabel("Epochs")
plt.ylabel("Difference between Weight Vectors")
plt.legend()
plt.savefig('Variance(MAP) 0.5.jpg')

plt.figure(2)
w_ml_r, weights_ml_r, ml_norm = Log_Regression(num_epochs,X_train,y_train,sig,g,w_ml,d)
ml_error_train = testing_error(w_ml_r,X_train,y_train)
ml_error_test = testing_error(w_ml_r,X_test,y_test)
print(ml_error_train)
print(ml_error_test)
plt.plot(range(len(ml_norm)),ml_norm,color='blue', label = "ML Estimate")
plt.xlabel("Epochs")
plt.ylabel("Difference between Weight Vectors")
plt.legend()
plt.savefig('Variance(ML) 0.5.jpg')

