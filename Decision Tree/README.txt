To run the decision tree ID3 algorithm, create an instance of the class and pass two arguments for desired depth and metric. 
The metric being passed is a string corresponding to the metric being used to split the data: 'Entropy', 'GI', or 'ME'. Call
the fit function on data wishing to be analyzed. Note, the inputs to the fit function are the raw data without labels,
the data labels, and a flags array. The flags array is an array of size equal to the number of features in the data being analyzed,
where a 0 is placed in elements where the feature is non-numerical and a 1 where the feature is numerical. Use the predict
function to predict outcomes on the "X" data in question. Located in the folder is also a "get_prediction_accuracy" function that
can be used to compare outcomes of the ID3 algorithm against the labels of the raw data. 

To use the ID3 class with the algorithms for homework 2 - AdaBoost and Bagged Trees, utilize the "ID3_class_weights" class which supports
weighted examples. 

To use the ID3 class with the algorithms for homework 2 - Random Forest, utilize the "ID3_class_bagged_trees" class which randomly
selects a subset of features before splitting. In this algorithm, located in the Ensemble folder, an extra parameter is passed 
corresponding to the size of the feature subset. 

Example calling ID3: 

flags =[0,1,0,...,1]
id3_example = ID3(max_depth=3,metric='Entropy')
id3_example.fit(X_train,y_train,flags)
y_train_hat = id3_example.predict(X_train)
y_test_hat = id3_example.predict(X_test)
print(f'training accuray: {get_prediction_accuracy(y_train,y_train_hat)}')
print(f'testing accuray: {get_prediction_accuracy(y_test,y_test_hat)}')
