# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 15:55:58 2021

@author: jagadeesan
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

from sklearn.model_selection import *
from sklearn.feature_selection import *
from sklearn.metrics import *
from scikitplot.metrics import plot_roc
from sklearn.preprocessing import *
from sklearn.ensemble import *
from sklearn.decomposition import PCA
from sklearn.naive_bayes import BernoulliNB

#Importing Dataset
dt = pd.read_csv("thai.csv")
dt.head()
dt.describe()

#Plotting Data
dt.hist(figsize=(40,60))
plt.show()# we can see most of the data are skewed

#UNDERSTANDING THE DATA
#Correlation of Data with Target Values
dt.corrwith(dt['Bankrupt?'])

#Checking the Presence of Null Values If Any
dt.isnull().sum()
dt.isna().sum()

#Reducing skewness using Log and Cube transfermation 
def corr_skew(X):
    s = X.skew().reset_index().rename(columns = {0:'skew'})

    pos = list(s[s['skew']>=1]['index'].values)
    neg = list(s[s['skew']<=-1]['index'].values)

    X[pos] = (X[pos]+1).apply(np.log)
    X[neg] = (X[neg])**3
    return X

y  = dt['Bankrupt?']
X  = dt.drop(['Bankrupt?'],axis=1)
X = corr_skew(X)


def plot_PCA(X,Y):
    
    pca = PCA()
    X = pca.fit_transform(X)

    # 2D plot
    plt.scatter(X[:,0],X[:,1],c=y,cmap=ListedColormap(['b','r']))
    plt.show()    

    # 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(X[:,0],X[:,1],X[:,2],c=y,cmap=ListedColormap(['b','r']))
    plt.show()

plot_PCA(X,y)

#Model Training

def pred_stratified(X,y):
    X = X.values#data
    y = y.values#target

    skf = StratifiedKFold(n_splits = 6)
    aucs = []
    fig, ax = plt.subplots()

    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        model = BernoulliNB(alpha = 10)
        model.fit(X_train,y_train)

        yxgb = model.predict(X_test)
        plot_roc(model, X_test, y_test, ax=ax)
        aucs.append(roc_auc_score(y_true=y_test,y_score=yxgb))
    plt.show()      
    return sum(aucs)/5


pred_stratified(X,y)

##Feature Selection to remove the unwanted features
sel = SelectFromModel(RandomForestClassifier(random_state=42))

y  = dt['Bankrupt?']
X  = dt.drop(['Bankrupt?'],axis=1)
X = corr_skew(X)
sel.fit(X,y)

features = X.columns[(sel.get_support())]
print(len(features))
features
X = X.filter(items=features)
plot_PCA(X,y)
pred_stratified(X,y)













