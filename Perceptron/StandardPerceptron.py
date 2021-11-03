#Ryan Miller
#Machine Learning 
#Homework Assignment 3
#Standard Percptron Algorithm 

import numpy as np 
import random
import pandas as pd

path1 = 'bank-note/test.csv'
path2 = 'bank-note/train.csv'
test_df = pd.read_csv(path1,header=None)
train_df = pd.read_csv(path2,header=None)

test_df.insert(loc=0,column='0',value=1)     
train_df.insert(loc=0,column='0',value=1)

X_train = (train_df.iloc[:,:-1]).values.tolist()
y_train_raw = (train_df.iloc[:,-1]).values.tolist()
dispatcher ={0:-1,1:1}
y_train = [dispatcher[lb] for lb in y_train_raw]
X_test = (test_df.iloc[:,:-1]).values.tolist()
y_test_raw = (test_df.iloc[:,-1]).values.tolist()
y_test = [dispatcher[lb] for lb in y_test_raw]

def Standard_PerceptronTrain(X_train,y_train,epochs,LR):
    
    w = np.zeros(len(X_train[0]))
    
    for t in range(epochs):
        random.shuffle(X_train)
        for i in range(len(X_train)):
            if (y_train[i]*np.matmul(w,np.transpose(np.asarray(X_train[i])))) <= 0:
                w = w + LR*y_train[i]*np.asarray(X_train[i])
    return w

def Standard_PerceptronTest(w, X_test, y_test):
    err = 0
    for i in range(len(X_test)):
        pred = np.sign(np.matmul(w,np.transpose(np.asarray(X_test[i]))))
        if pred != y_test[i]:
            err = err+1
    
    return err/len(X_test)
    
w = Standard_PerceptronTrain(X_train,y_train,epochs=10,LR = .1)
test_err = Standard_PerceptronTest(w, X_test, y_test)
print('Learned Weight vector:')
print(w)
print('Testing Error:')
print(test_err)