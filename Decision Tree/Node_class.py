#Ryan Miller
#Machine Learning 
#Homework Assignment 1
#Problems 1 and 2

#ID3 algorithim steps 
#define NODE class, recursive for branch children  -> this file and then import to ID3 class file
#define ID3 class, takes in depth and metric parameters 
    #inside class, functions defined for each metric (entropy, gini, and ME)
    #following algorithm archietecutre, includes fit and predict functions 
    #seperate gain function for numerical features
    #takes in flag array which is set to 0 for non-numerical feature and 1 for numerical feature 
    
import random 

#Node class
class NODE:
  def __init__(self,branches=[],is_leaf=True):
    self.is_leaf = is_leaf
    self.branches = branches
    self.num_childs = len(branches)
    self.childs ={}
    if self.num_childs > 0:
      self.is_leaf = False
      for branch in self.branches:
        self.childs[branch] = NODE()

    def default_branch_fn(self,x):
      if not self.is_leaf:
        return random.choice(self.branches)

    def default_label_fn(self,x):
      if self.is_leaf:
        return None

    if self.is_leaf:
      self.label_fn = default_label_fn
    else:
      self.branch_fn = default_branch_fn


  def __getitem__(self,idx):
    if not self.is_leaf:
      return self.childs[idx]

  def __setitem__(self,idx,node):
    if not self.is_leaf:
      self.childs[idx] = node

  def set_branch_fn(self,func):
    if not self.is_leaf:
      self.branch_fn = func

  def set_label_fn(self,func):
    if self.is_leaf:
      self.label_fn = func

  def set_branches(self,branches):
    self.__init__(branches=branches)


  def make_single_decision(self,x):
    if self.is_leaf:
      return self.label_fn(self,x)
    else:
      branch = self.branch_fn(self,x)
      return self.childs[branch].make_single_decision(x)

  def make_decision(self,X):
    decisions =[]
    for x in X:
      this_decision = self.make_single_decision(x)
      decisions.append(this_decision)
    return decisions
    
  def get_structure(self):
    if self.is_leaf:
      return {'Leaf Node'}
    else:
      return {branch:self.childs[branch].get_structure() for branch in self.branches}
        
    
    
    