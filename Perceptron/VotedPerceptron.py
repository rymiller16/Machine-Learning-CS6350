#Ryan Miller
#Machine Learning 
#Homework Assignment 3
#Voted Percptron Algorithm 

import numpy as np 
import pandas as pd
import csv

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

def Voted_PerceptronTrain(X_train,y_train,epochs,LR):
    w = {}
    w[0] = np.zeros(len(X_train[0]))
    m = 0 
    C = {}
    
    for t in range(epochs):
        for i in range(len(X_train)):
            if (y_train[i]*np.matmul(w[m],np.transpose(np.asarray(X_train[i])))) <= 0:
                w[m+1] = w[m] + LR*y_train[i]*np.asarray(X_train[i])
                m = m + 1
                C[m] = 1
            else: 
                C[m] = C[m]+1
    
    return w, C

def Voted_PerceptronTest(w, C, X_test, y_test):
    err = 0
    sum = 0
    for i in range(len(X_test)):
        for k in range(1,len(w)):#range(1,len(w)-1):
            _ = C[k]*np.sign(np.matmul(w[k],np.transpose(np.asarray(X_train[i]))))
            sum = sum + _
        pred = np.sign(sum)
        sum = 0
        if pred != y_test[i]:
            err = err+1
            
    return err/len(X_test)

w, C = Voted_PerceptronTrain(X_train,y_train,epochs = 10,LR = 0.1)
test_err = Voted_PerceptronTest(w,C,X_test,y_test)

print('Weight vector followed by count:')
with open('Voted_Perceptron_results.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Weight Vector','Counts'])
    for i in range(1,len(w)):
        writer.writerow([w[i],C[i]])
print('Test Error:')
print(test_err)
