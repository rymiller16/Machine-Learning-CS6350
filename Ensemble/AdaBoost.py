#Ryan Miller
#Machine Learning 
#Homework Assignment 2
#AdaBoost Algorithim 

from ID3_class_weights import ID3 
import numpy as np 

def corr_fn(y,y_hat):
    corr = []
    for i in range(len(y)):
        corr.append(y[i]*y_hat[i])
    return corr

def adaboost(X_train,y_train,flags,X_test,y_test,iter=50):
    w_train = len(y_train)*[1/len(y_train)]
    y_train_hat_ensemble = np.zeros(len(y_train))
    y_test_hat_ensemble = np.zeros(len(y_test))
    train_errs = []
    test_errs = []
    train_errs_ensemble = []
    test_errs_ensemble = []
  
    for t in range(iter):
        this_id3 = ID3(max_depth=2,metric='Entropy')
        this_id3.fit(X_train,y_train,w_train,flags)
        
        y_train_hat = this_id3.predict(X_train)
        y_test_hat = this_id3.predict(X_test)
        
        corr_train = corr_fn(y_train,y_train_hat)
        corr_test = corr_fn(y_test,y_test_hat)
        
        eps_train = 0.5 - 0.5*np.sum(np.array(w_train)*np.array(corr_train))
        eps_test = 0.5 - 0.5*np.mean(np.array(corr_test))
        
        train_errs.append(eps_train)
        test_errs.append(eps_test)
        
        alpha_t = 0.5*np.log((1-eps_train)/(eps_train+0.000001))
        w_new = np.array(w_train)*np.exp(-alpha_t*np.array(corr_train))
        w_train = [weight/np.sum(w_new) for weight in w_new]
        
        y_train_hat_ensemble += alpha_t*np.array(y_train_hat)
        y_test_hat_ensemble += alpha_t*np.array(y_test_hat)
        
        corr_train_ensemble = corr_fn(y_train,np.sign(y_train_hat_ensemble))
        corr_test_ensemble = corr_fn(y_test,np.sign(y_test_hat_ensemble))
        
        eps_train_ensemble = 0.5 - 0.5*np.mean(np.array(corr_train_ensemble))
        eps_test_ensemble = 0.5 - 0.5*np.mean(np.array(corr_test_ensemble))
        
        train_errs_ensemble.append(eps_train_ensemble)
        test_errs_ensemble.append(eps_test_ensemble)

    return train_errs, test_errs, train_errs_ensemble, test_errs_ensemble




