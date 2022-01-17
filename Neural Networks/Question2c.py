#Ryan Miller
#Machine Learning
#Assignment 5
#Question 2c - Neural Network with Pytorch

import torch as T
import numpy as np 
import pandas as pd
import torch.nn as nn 
import torch.nn.functional as F

path1 = 'bank-note/test.csv'
path2 = 'bank-note/train.csv'
test_df = pd.read_csv(path1,header=None)
train_df = pd.read_csv(path2,header=None)

X_train = (train_df.iloc[:,:-1]).values.tolist()
y_train_raw = (train_df.iloc[:,-1]).values.tolist()
dispatcher ={0:0,1:1}
y_train = [dispatcher[lb] for lb in y_train_raw]
X_test = (test_df.iloc[:,:-1]).values.tolist()
y_test_raw = (test_df.iloc[:,-1]).values.tolist()
y_test = [dispatcher[lb] for lb in y_test_raw]

X_train = np.array(X_train)
X_test = np.array(X_test)
y_test = np.array(y_test)
y_train = np.array(y_train)
y_train = np.reshape(y_train,(len(y_train),1))
y_test = np.reshape(y_test,(len(y_test),1))

def accuracy(model, x, y):
  X = T.Tensor(x)
  Y = T.ByteTensor(y)   
  ouput = model(X)            
  pred_y = ouput >= 0.5   
  num_correct = T.sum(Y==pred_y) 
  N = len(y)
  acc = (num_correct / N)  # scalar
  return acc

class Net(T.nn.Module):
  def __init__(self):
    super(Net, self).__init__()
    
    width = 100
    self.layer1 = T.nn.Linear(4, width)  
    self.layer2 = T.nn.Linear(width, width)
    self.layer3 = T.nn.Linear(width, width)  
    self.layer4 = T.nn.Linear(width, width)
    self.layer5 = T.nn.Linear(width, width)  
    self.layer6 = T.nn.Linear(width, width)
    self.layer7 = T.nn.Linear(width, width)  
    self.layer8 = T.nn.Linear(width, width)
    self.layer_out = T.nn.Linear(width, 1)
    
    T.nn.init.xavier_uniform_(self.layer1.weight)
    T.nn.init.zeros_(self.layer1.bias)
    T.nn.init.xavier_uniform_(self.layer2.weight)
    T.nn.init.zeros_(self.layer2.bias)
    T.nn.init.xavier_uniform_(self.layer3.weight)
    T.nn.init.zeros_(self.layer3.bias)
    T.nn.init.xavier_uniform_(self.layer4.weight)
    T.nn.init.zeros_(self.layer4.bias)
    T.nn.init.xavier_uniform_(self.layer5.weight)
    T.nn.init.zeros_(self.layer5.bias)
    T.nn.init.xavier_uniform_(self.layer6.weight)
    T.nn.init.zeros_(self.layer6.bias)
    T.nn.init.xavier_uniform_(self.layer7.weight)
    T.nn.init.zeros_(self.layer7.bias)
    T.nn.init.xavier_uniform_(self.layer8.weight)
    T.nn.init.zeros_(self.layer8.bias)
    T.nn.init.xavier_uniform_(self.layer_out.weight)
    T.nn.init.zeros_(self.layer_out.bias)
    
  def forward(self, inputs):
    x = T.tanh(self.layer1(inputs))
    x = T.relu(self.layer2(x))
    x = T.relu(self.layer3(x))
    x = T.relu(self.layer4(x))
    x = T.relu(self.layer5(x))
    x = T.relu(self.layer6(x))
    x = T.relu(self.layer7(x))
    x = T.relu(self.layer8(x))
    x = T.sigmoid(self.layer_out(x))
    return x
    
def main():
  net = Net()
  loss_fn = T.nn.BCELoss()  
  optimizer = T.optim.Adam(net.parameters(), lr=10e-3)
  
  for epoch in range(100):
    if epoch % 10 == 0:
      print('epoch = %4d' % epoch)
      acc = accuracy(net, X_train, y_train)
      print('accuracy = %0.4f (Training Data)' % acc)
    for i in range(100):
      X_i = T.Tensor(X_train[i])
      y_i = T.Tensor(y_train[i])
      optimizer.zero_grad()
      ouput = net(X_i)
      loss_obj = loss_fn(ouput, y_i)
      loss_obj.backward()
      optimizer.step()
 
  acc_test = accuracy(net, X_test, y_test)
  print('Testing Accuracy = %0.4f' % acc_test)

if __name__=='__main__':
  main()