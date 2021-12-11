#Ryan Miller
#Machine Learning 
#Back Propogation Algo 

import numpy as np 
import pandas as pd
from random import random

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

#parameters
num_HL = 2                  #number of hidden layers
num_inputs = len(X_train[0])              #number of inputs (including biases)
num_outputs = 1             #number of outputs
num_layers = 3              #number of layers
width = 5                   #width of units in hidden layers
example_num = 0

weights_1 = {}
weights_2 = {}
weights_3 = {}
inputs = [1,1,1,1,1]

for i in range(num_layers):
    weights_1[i] = {}
    weights_2[i] = {}
    weights_3[i] = {}
    for j in range(width):
        weights_1[i][j+1] = {}
        weights_2[i][j+1] = {}
for i in range(num_layers):
    for j in range(width):
        weights_1[i][j+1] = random()
        weights_2[i][j+1] = random()

output = 0
#Forward propogation
for i in range(1,width+1):
    for j in range(1,num_layers+1):
        if j == 1:
            output = output + (inputs[i-1] * weights_1[j][i])
        if j == 2:
            output = output + (inputs[i-1] * weights_2[j][i])
            
def derivative(inputs,outputs):
    return (inputs - outputs)/2

def activation(inputs,outputs):
    return (1)/(1-np.exp(inputs/outputs))

#Backward Propogation to get derivatives
weights = np.random.uniform(0,1,(num_layers,width))
for i in range(0,num_layers):
    for j in range(1,width):
        if j == 1:
            weights[j,i-1] = (weights_1[i][j] - output)/2
        if j == 2:
            weights[j,i-1] = (weights_2[i][j] - output)/2
        if j == 2:
            weights[j,i-1] = (weights_2[i][j] - output)/2
        








    

