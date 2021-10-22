#Ryan Miller
#Machine Learning 
#Homework Assignment 2
#Problem 4

#Part a/b -> Batch Gradient Descent and Stochastic Gradient Descent

import numpy as np 

def cost_fn(weight_v,X,y,counter):
  m = len(X)
  sum = 0

  for i in range(m):
    error = (y[i] - np.dot(weight_v[counter],np.array([X[i]]).T))
    error = error[0]
    inside_sum = error ** 2
    sum = sum + inside_sum
  
  sum = sum / 2

  return sum

def grad_J_wt(weight_v,X,y,idx,counter):
  m = len(X)
  sum = 0

  for i in range(m):
    error = (y[i] - np.dot(weight_v[counter],np.array([X[i]]).T))
    error = error[0]
    xij = X[i][idx]
    inside_sum = np.dot(error,xij)
    sum = sum + inside_sum
  
  sum = -sum
    
  return sum

def grad_J_vector_fn(weight_v,X,y,counter): 
  num_weights = 8
  grad_vector = []

  for idx in range(num_weights):
    grad_vector.append(grad_J_wt(weight_v,X,y,idx,counter))

  return grad_vector

def error_difference(weight_v, counter):
  wt = weight_v[counter]
  wt_1 = weight_v[counter-1]
  inside = wt - wt_1
  the_norm = np.linalg.norm(inside)

  return the_norm

def batch_gradient_descent(X,y,LR):

  counter = 0
  grad_J_v = {}
  weight_v = {}
  error_v = {}
  cost = {}
  
  while(1):

    if counter == 0:
      weight_v [counter] = np.zeros(len(X[0]))                                      
      cost [counter] = cost_fn(weight_v, X, y, counter)                               
      grad_J_v [counter] = grad_J_vector_fn(weight_v, X, y, counter)                
      counter = counter + 1
    else: 
      weight_v [counter] = weight_v [counter-1] - np.dot(LR,grad_J_v[counter-1])    
      cost [counter] = cost_fn(weight_v, X,y, counter)                              
      grad_J_v [counter] = grad_J_vector_fn(weight_v, X, y, counter)                                                                          
      error_v[counter] = error_difference(weight_v,counter)                         
      if (error_difference(weight_v, counter) < 10e-6):
        print("We have converged")
        break
      else:
        counter = counter + 1

  return counter, grad_J_v, weight_v, error_v, cost

def update_weights_fn(counter, X, y, sample_idx, idx, weight_v, LR):
    error = (y[sample_idx] - np.dot(weight_v[counter],np.array([X[sample_idx]]).T))
    error = error[0]
    xij = X[sample_idx][idx]
    inside_sum = np.dot(error,xij)
    outside_sum = np.dot(inside_sum,LR)
    weight = weight_v[counter][idx]+outside_sum   

    return weight

def update_weights(counter, X, y, sample_idx, weight_v, LR):
  num_weights = 8
  weight_vector = []

  for idx in range(num_weights):
    weight_vector.append(update_weights_fn(counter, X, y, sample_idx, idx, weight_v, LR))
  
  weight_vector = np.asarray(weight_vector)
  return weight_vector

def stoch_gradient_descent(X,y,LR):

  counter = 0
  weight_v = {}
  error_v = {}
  cost = {}
  
  while(1):

    sample_idx = np.random.choice(len(X), size = 1)                   
    sample_idx = sample_idx[0]                                     

    if counter == 0:
      weight_v [counter] = np.zeros(len(X[0]))                          
      cost [counter] = cost_fn(weight_v, X, y, counter)                 
      counter = counter+1
    else:
      weight_v [counter] = update_weights(counter-1,X,y,sample_idx,weight_v, LR)   
      cost [counter] = cost_fn(weight_v, X, y, counter)
      error_v[counter] = error_difference(weight_v,counter)

      placeholder = [*cost.values()]
      cost_at_counter = (placeholder[counter])

      if ((cost_at_counter) < 15.4):
        print("We have converged")
        break
      else:
        counter = counter + 1

  return counter, weight_v, error_v, cost



