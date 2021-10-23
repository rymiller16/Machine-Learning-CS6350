Located in this folder are the Adaboost, Bagged Trees, and Random Forest Algorithims. 

AdaBoost: The Adaboost algorithm takes in training data (X then Y), flags, testing data (X then Y), number of iterations (5 in total, in that order).
Note the y data in the form of -1 and 1's. 

Example usage: 
path1 = "bank/test.csv"
path2 = "bank/train.csv"
header_list = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','label']
test_df = pd.read_csv(path1)
train_df = pd.read_csv(path2)
test_df.columns = header_list
train_df.columns = header_list

X_train = (train_df.iloc[:,:-1]).values.tolist()
y_train_raw = (train_df.iloc[:,-1]).values.tolist()
dispatcher ={'no':1,'yes':-1}
y_train = [dispatcher[lb] for lb in y_train_raw]
flags =[1,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0]
X_test = (test_df.iloc[:,:-1]).values.tolist()
y_test_raw = (test_df.iloc[:,-1]).values.tolist()
y_test = [dispatcher[lb] for lb in y_test_raw]

train_errs, test_errs, train_errs_ensemble, test_errs_ensemble = adaboost(X_train,y_train,flags,X_test,y_test,iter=500)

/////////
Bagged Trees: The Bagged Trees algorithm takes in training data (X then Y), flags, testing data (X then Y), number of iterations (5 in total, in that order). 
Note the y data in the form of -1 and 1's. 

Example usage: 
path1 = "bank/test.csv"
path2 = "bank/train.csv"
header_list = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','label']
test_df = pd.read_csv(path1)
train_df = pd.read_csv(path2)
test_df.columns = header_list
train_df.columns = header_list

X_train = (train_df.iloc[:,:-1]).values.tolist()
y_train_raw = (train_df.iloc[:,-1]).values.tolist()
dispatcher ={'no':1,'yes':-1}
y_train = [dispatcher[lb] for lb in y_train_raw]
flags =[1,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0]
X_test = (test_df.iloc[:,:-1]).values.tolist()
y_test_raw = (test_df.iloc[:,-1]).values.tolist()
y_test = [dispatcher[lb] for lb in y_test_raw]

train_errs, test_errs, train_errs_ensemble, test_errs_ensemble = bagging(X_train,y_train,flags,X_test,y_test,iter=500)

/////////
Random Forest: The Random Forest algorithm takes in training data (X then Y), flags, testing data (X then Y), size of feature subset, number of iterations (6
in total, in that order). Note the y data in the form -1 and 1's. 

Example usage: 
path1 = "bank/test.csv"
path2 = "bank/train.csv"
header_list = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','label']
test_df = pd.read_csv(path1)
train_df = pd.read_csv(path2)
test_df.columns = header_list
train_df.columns = header_list

X_train = (train_df.iloc[:,:-1]).values.tolist()
y_train_raw = (train_df.iloc[:,-1]).values.tolist()
dispatcher ={'no':1,'yes':-1}
y_train = [dispatcher[lb] for lb in y_train_raw]
flags =[1,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0]
X_test = (test_df.iloc[:,:-1]).values.tolist()
y_test_raw = (test_df.iloc[:,-1]).values.tolist()
y_test = [dispatcher[lb] for lb in y_test_raw]

#For feature subset size 2
train_errs, test_errs, train_errs_ensemble, test_errs_ensemble = randforest(X_train,y_train,flags,X_test,y_test,2,iter=500)
