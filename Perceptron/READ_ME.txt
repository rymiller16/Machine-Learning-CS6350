To run the percpetron algorithms, solely run the shell script provided. This is enough to compare results of homework 3 with my report. 
If you would like more details, read below. I have included the data assignments in case the shell script does not work (I have tested it on my end 
but sometimes get some weird message when running on CADE). Thus, worst case include the bank note csv files in your working directory and run the three
scripts that are located in the "Perceptron" folder. Note: the voted Perceptron algorithm reports its weight vectors and counts by writing to a csv file that 
can be found in your working directory after the script has finished running.

1) Standard Perceptron:
The standard perceptron algorithm is included in a script that calls the function on bank note data. If you wish to change the data set upon 
which the algorithm runs on, simply pass in training data, number of epochs, and the learning rate. The standard percpetron file included in the 
folder also includes a function that computes testing error using the learned weight vector. Note the y data for training should be in form {-1,1}.

Example calling:
w = Standard_PerceptronTrain(X_train,y_train,epochs=10,LR = .1)
test_err = Standard_PerceptronTest(w, X_test, y_test)

2) Averaged Perceptron:
Same details as Standard Perceptron. Pass learned a vector into testing function. 

Example calling: 
a = Averaged_PerceptronTrain(X_train,y_train,epochs = 10,LR = 0.1)
test_err = Averaged_PerceptronTest(a,X_test,y_test)

3) Voted Perceptron: 
Same details as Standard Perceptron. Pass learned weight and counts into testing function. Note, results are written to CSV file located in working directory.

Example calling: 
w, C = Voted_PerceptronTrain(X_train,y_train,epochs = 10,LR = 0.1)
test_err = Voted_PerceptronTest(w,C,X_test,y_test)
