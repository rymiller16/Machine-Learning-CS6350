#Ryan Miller
#Machine Learning 
#Assingment 4 
#Programming Problem 3b

import numpy as np 
import pandas as pd
from scipy.optimize import minimize 

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

C_list = [100/873, 500/873, 700/873]
C = C_list[0]
#gamma = 0.1
gamma = 0.5
#gamma = 1
#gamma = 5
#gamma = 100

def gaussian_kernel(alphas,X,y):
    X = np.matrix(X)
    y = np.asarray(y)
    N = len(X)
    
    IP = 0
    matrix1 = np.sum(np.multiply(X,X),axis=1)
    matrix1 = np.tile((matrix1), (1, N))
    matrix2 = np.transpose(matrix1)
    matrix3 = 2*X@X.T
    IP1 = np.add(matrix1,matrix2)
    IP1 = np.subtract(IP1,matrix3)
    IP1 = IP1**2
    IP1 = np.multiply(-1,IP1)
    matrix3 = np.exp(IP1/gamma)
    matrix1 = np.outer(alphas,y)
    matrix2 = matrix1
    matrix2 = np.transpose(matrix2)
    matmul1 = np.multiply(matrix1,matrix2)
    matmul2 = np.multiply(matmul1,matrix3)
    IP = np.sum(matmul2)
    return 0.5*IP

def second_cost(alphas):
	return -np.sum(alphas)

y_train1 = np.asarray(y_train)
cost_fn = lambda alphas: gaussian_kernel(alphas,X_train,y_train) + second_cost(alphas)
constraint_1 = lambda alphas: np.dot(alphas.T,y_train)
constraint_2 = lambda alphas: C-alphas
constraint_3 = lambda alphas: alphas #-0.0001

cons = ({'type':'eq','fun':constraint_1},
        {'type':'ineq','fun':constraint_2},
        {'type':'ineq','fun':constraint_3})

alpha_int = np.ones(y_train1.shape)

sol = minimize(fun = cost_fn, x0 = alpha_int, method = 'SLSQP', constraints = cons)

#extract support vectors 
support_v = sol.x

support_idx = (sol.x > 0.001)

X_train1 = np.asarray(X_train)
alpha_v = sol.x[support_idx]
y_v = y_train1[support_idx]
X_v = X_train1[support_idx,:]

w_star = np.sum(alpha_v*y_v*X_v.T, axis=1)

def SVM_prediction(w_star, X_test, y_test):
    err = 0
    w_star = w_star.reshape(1,-1)
    X_test = np.asarray(X_test)
    for i in range(0,len(X_test)-1):
        pred = np.sign(np.dot(w_star,X_test[i]))
        if pred != y_test[i]:
            err = err+1
    return err/len(X_test)

training_err = SVM_prediction(w_star,X_train,y_train)
print("Training Error: ")
print(training_err)
print('\n')
testing_err = SVM_prediction(w_star,X_test,y_test)
print("Testing Error: ")
print(testing_err)
print(len(support_idx))
    

    
