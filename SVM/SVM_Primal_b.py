#Ryan Miller
#Machine Learning 
#Assingment 4 
#Programming Problem 2b

import numpy as np 
import pandas as pd
import random
import matplotlib.pyplot as plt

path1 = 'bank-note/test.csv'
path2 = 'bank-note/train.csv'
test_df = pd.read_csv(path1,header=None)
train_df = pd.read_csv(path2,header=None)

test_df.insert(loc=4,column='4',value=1)     #setting bias
train_df.insert(loc=4,column='4',value=1)

X_train = (train_df.iloc[:,:-1]).values.tolist()
y_train_raw = (train_df.iloc[:,-1]).values.tolist()
dispatcher ={0:-1,1:1}
y_train = [dispatcher[lb] for lb in y_train_raw]
X_test = (test_df.iloc[:,:-1]).values.tolist()
y_test_raw = (test_df.iloc[:,-1]).values.tolist()
y_test = [dispatcher[lb] for lb in y_test_raw]

def SVM_SSGD(X,y,num_Epochs,C,gamma_o):
    norm_v = np.zeros(num_Epochs)
    w_add = [0]
    N = len(X)
    w = np.zeros(len(X[0]))
    
    for i in range(1,num_Epochs):
        gamma_t = (gamma_o)/(1+i)
        
        norm = np.linalg.norm(w)
        norm_v[i-1] = norm
        
        if i != 1:
            if norm < 0.00001:
                print("We have converged")
                return w
        
        print(norm)
        random.shuffle(X)
        for j in range(0,len(X)-1):
            if (y[j]*np.matmul(w,np.transpose(np.asarray(X[j])))) <= 1:
                idx = len(w)-1
                w_0 = np.delete(w,idx,0)
                w_1 = np.append(w_0,w_add)
                w = w - gamma_t*w_1 + gamma_t*C*N*y[j]*np.asarray(X[j])
            else: 
                w_0 = (1-gamma_t)*w_0
    return w, norm_v

def testing_error(w,X,y):
    err = 0
    for i in range(len(X)):
        pred = np.sign(np.matmul(w,np.transpose(np.asarray(X[i]))))
        if pred != y[i]:
            err = err+1
    return err/len(X)
    

num_Epochs = 100
C = [100/873, 500/873, 700/873]
C = C[2]
gamma_o = 0.01
w, norm_v = SVM_SSGD(X_train,y_train,num_Epochs,C,gamma_o)
train_err = testing_error(w,X_train,y_train)
test_err = testing_error(w,X_test,y_test)
print("Testing Error: ")
print(test_err)
print("Training Error: ")
print(train_err)
print("C: ")
print(C)
print("weight Vector: ")
print(w)
print("Gamma: ")
print(gamma_o)

plt.plot(range(len(norm_v)),norm_v,color='red')
plt.title('SVM: Primal')
plt.xlabel('Epochs')
plt.ylabel('Difference in weight Vector')
plt.savefig('Results - SVM (Error vs Iterations)')
plt.show()