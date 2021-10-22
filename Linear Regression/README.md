Read Me File: 

In "Gradient Descent" there is one file containing both Batch and Stochastic Gradient Descent Algorithms. To use these algorithms, the user must declare the data set in X and Y
to be tested. The user must also pass through a learning rate upon which to test the algorith. Both algorithms output 4 variables: counter, weights, error, and cost. The weights,
error, and cost are all python dictionaries and data must be extracted as such. Below is an example on how to call and extract the information from the Batch Gradient Descent
Algorithm. To utilize the Stochastic Gradient Descent Algorith, simply replace the "batch_gradient_descent" function call with "stoch_gradient_descent". Enjoy. 

Example Usage: 

path1 = 'concrete/test.csv'
path2 = 'concrete/train.csv'
test_df = pd.read_csv(path1,header=None)
train_df = pd.read_csv(path2,header=None)

test_df.insert(loc=0,column='0',value=1)     
train_df.insert(loc=0,column='0',value=1)

X_train = (train_df.iloc[:,:-1]).values.tolist()   
y_train = (train_df.iloc[:,-1]).values.tolist()    
X_test = (test_df.iloc[:,:-1]).values.tolist()
y_test = (test_df.iloc[:,-1]).values.tolist()  

LR = .00001
print('\n')
count, J_v, weights_v, error_v, cost = batch_gradient_descent(X_train,y_train,LR)       
print('Converged at iteration number:', count)
print('\n')
weights = np.ndarray.tolist(weights_v[count])
print('The weight vector at convergence is:', weights)

placeholder = [*cost.values()]
cost_at_counter2 = (placeholder[count])

print('\n')
print('Cost value at convergence (Batch):', cost_at_counter2)

testing_cost = cost_fn_testing(weights, X_test, y_test)
print('\n')
print('Cost of testing data: ', testing_cost)

y = [*cost.values()]
x = [*cost.keys()]

#cost vs iteration
plt.plot(x,y,'-b')
plt.title('Batch Gradient Descent: Training Data')
plt.xlabel('Number of Iterations')
plt.ylabel('Cost')
plt.savefig('Results - Batch Gradient Descent.png')
plt.show()
