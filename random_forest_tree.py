# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:39:50 2023

@author: Divyasri
"""

import pandas as pd
data=pd.read_csv(r"C:\Users\Divyasri\OneDrive\Desktop\AIML\iris.csv")
data.head()

data.dropna(inplace=True)

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred))