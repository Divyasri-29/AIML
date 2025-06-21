# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:17:07 2023

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

##Decision Tree classifier
#from sklearn.tree import DecisionTreeClassifier
#model=DecisionTreeClassifier(criterion='entropy')

#Random Forest
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()

##logistic regression
#from sklearn.linear_model import LogisticRegression
#model=LogisticRegression()

##support vector
#from sklearn.svm import SVC
#model=SVC()

##naive bayes
#from sklearn.naive_bayes import GaussianNB
#model=GaussianNB()

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred))

print(model.predict([[1.2,1.3,1.4,1.5]]))