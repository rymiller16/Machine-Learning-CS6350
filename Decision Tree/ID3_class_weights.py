#Ryan Miller
#Machine Learning 
#Homework Assignment 2
#ID3 algorithim for AdaBoost and Bagged Trees 

import numpy as np 
from Node_class import NODE

class ID3:
  def __init__(self,max_depth=0,metric ='Entropy'):
    self.max_depth = max_depth
    self.minimum_metric = 0.00001
    self.metric = metric
    self.tree = NODE()

    def entropy(labels, weights):
      y = list(labels)
      w = list(weights)
      unique_labels = list(set(y))
      prob =[sum([w[i] for i in range(len(y)) if y[i]==lb])/sum(w) for lb in unique_labels]
      if len(prob)>0:
        ent = -np.sum(np.array(prob)*np.log2(np.array(prob)))
      else:
        ent = 0
      return ent

    def majority_error(labels, weights):
      y = list(labels)
      w = list(weights)
      unique_labels = list(set(y))
      prob =[sum([w[i] for i in range(len(y)) if y[i]==lb])/sum(w) for lb in unique_labels]
      if len(prob)>0:
        me = 1-np.max(np.array(prob))
      else:
        me = 0

      return me

    def gini_index(labels, weights):
      y = list(labels)
      w = list(weights)
      unique_labels = list(set(y))
      prob =[sum([w[i] for i in range(len(y)) if y[i]==lb])/sum(w) for lb in unique_labels]
      if len(prob)>0:
        gi = 1-np.sum(np.array(prob)**2)
      else:
        gi = 0
      return gi

    if self.metric =='Entropy':
      self.metric_fn = entropy
    elif self.metric == 'ME':
      self.metric_fn = majority_error
    elif self.metric == 'GI':
      self.metric_fn = gini_index

  def predict(self,X):
    return self.tree.make_decision(X)

  def gain_fn(self,S,attrib_idx, return_split=False):
    X = S[0]
    y = S[1]
    w = S[2]
    gain = self.metric_fn(y,w)
    unique_vals = list(set([x[attrib_idx] for x in X]))
    split ={}
    for val in unique_vals:
      y_v = [y[idx] for idx in range(len(X)) if X[idx][attrib_idx]==val]
      w_v = [w[idx] for idx in range(len(X)) if X[idx][attrib_idx]==val]
      X_v = [X[idx] for idx in range(len(X)) if X[idx][attrib_idx]==val]

      this_metric = self.metric_fn(y_v,w_v)
      gain -= (sum(w_v)/sum(w))*this_metric
      split[val] = ([X_v,y_v,w_v],this_metric)
    if not return_split:
      return gain
    else:
      return gain, split

  def gain_fn_num(self,S,attrib_idx, return_split=False):
    X = S[0]
    y = S[1]
    w = S[2]
    
    attrib_vals = [x[attrib_idx] for x in X]
    th_median = np.median(np.array(attrib_vals))
    
    y_v = [y[idx] for idx in range(len(X)) if X[idx][attrib_idx]>=th_median]
    y_v_cmp = [y[idx] for idx in range(len(X)) if X[idx][attrib_idx]<th_median]

    w_v = [w[idx] for idx in range(len(X)) if X[idx][attrib_idx]>=th_median]
    w_v_cmp = [w[idx] for idx in range(len(X)) if X[idx][attrib_idx]<th_median]
    
    X_v = [X[idx] for idx in range(len(X)) if X[idx][attrib_idx]>=th_median]
    X_v_cmp = [X[idx] for idx in range(len(X)) if X[idx][attrib_idx]<th_median]

    y_v_metric = self.metric_fn(y_v,w_v)
    y_v_cmp_metric = self.metric_fn(y_v_cmp,w_v_cmp)
    gain_th = self.metric_fn(y,w) -(sum(w_v)/sum(w))*y_v_metric - (sum(w_v_cmp)/sum(w))*y_v_cmp_metric

    key_v = f'above_{th_median:.2f}'
    key_v_cmp = f'below_{th_median:.2f}'
    split = {key_v:([X_v,y_v,w_v],y_v_metric),key_v_cmp:([X_v_cmp,y_v_cmp,w_v_cmp],y_v_cmp_metric),'th':th_median}

    if not return_split:
      return gain_th
    else:
      return gain_th, split

  def return_split(self,S,attrib_idxs,attrib_flags):
    gains = []
    for idx,flag in zip(attrib_idxs,attrib_flags):
      if flag==0:
        this_gain = self.gain_fn(S,idx)
      else:
        this_gain = self.gain_fn_num(S,idx)
      gains.append(this_gain)
    idx_max = attrib_idxs[np.argmax(np.array(gains))]
    flag_max = attrib_flags[np.argmax(np.array(gains))]
    if flag_max==0:
      gain_max, split_max = self.gain_fn(S,idx_max,return_split=True)
    else:
      gain_max, split_max = self.gain_fn_num(S,idx_max,return_split=True)
    
    return idx_max, split_max

  def make_label_fn(self,label):
    def label_fn(self,x):
      if self.is_leaf:
        return label
    return label_fn

  def make_branch_fn(self,idx):
    def branch_fn(self,x):
      if not self.is_leaf:
        return x[idx]
    return branch_fn

  def make_branch_fn_num(self,idx,th):
    def branch_fn(self,x):
      if not self.is_leaf:
        if x[idx] >= th:
          return f'above_{th:.2f}'
        else:
          return f'below_{th:.2f}'
    return branch_fn


  def fit(self,X,y,w,flags):
    self.tree = NODE()
    self.depth = 0
    self.num_features = len(X[0])
    self.labels = list(set(y))
    self.labels_prob = [sum([w[i] for i in range(len(y)) if y[i]==lb])/sum(w) for lb in self.labels]
    self.most_common_label = self.labels[np.argmax(np.array(self.labels_prob))]
    self.feature_vals = {}
    for idx in range(self.num_features):
      if flags[idx]==0:
        self.feature_vals[idx] = list(set([x[idx] for x in X]))

    if self.max_depth == 0:
      A = self.most_common_label
      self.tree.set_label_fn(self.make_label_fn(A))

    else:
      current_nodes =[self.tree]
      current_S = [([X,y,w],self.metric_fn(y,w))]
      current_idxs = range(self.num_features)
      current_flags = flags

      while len(current_nodes) > 0 and self.depth <= self.max_depth:
       
        assert(len(current_S) == len(current_nodes))
        new_nodes = []
        new_S = []
        
        for v in range(len(current_nodes)):

          S_v, metric_v = current_S[v]
          node_v = current_nodes[v]
          if (metric_v < self.minimum_metric) or (self.depth == self.max_depth):

            y_v = S_v[1]
            w_v = S_v[2]
            y_v_labels = list(set(y_v))
            y_v_probs = [sum([w_v[i] for i in range(len(y_v)) if y_v[i]==lb])/sum(w_v) for lb in y_v_labels]
            if len(y_v_probs) > 0:
              A = y_v_labels[np.argmax(np.array(y_v_probs))]
            else:
              A = self.most_common_label
            node_v.set_label_fn(self.make_label_fn(A))
            
          else:
            
            idx_v , this_split = self.return_split(S_v,current_idxs,current_flags)
            flag_v = current_flags[current_idxs.index(idx_v)]
            if flag_v==0:
              brns = self.feature_vals[idx_v]
            else:
              brns = this_split.keys()-{'th'}
  
            node_v.set_branches(brns)
            if flag_v==0:
              node_v.set_branch_fn(self.make_branch_fn(idx_v))
            else:
              node_v.set_branch_fn(self.make_branch_fn_num(idx_v,this_split['th']))
            

            for brn in brns:
              if not brn in this_split.keys():
                A = self.most_common_label
                node_v[brn].set_label_fn(self.make_label_fn(A))
              else:
                new_nodes.append(node_v[brn])
                new_S.append(this_split[brn])
 
        self.depth +=1
        current_nodes = new_nodes
        current_S = new_S

  
    
