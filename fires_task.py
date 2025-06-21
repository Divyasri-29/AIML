# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:54:16 2023

@author: Divyasri
"""

import pandas as pd
data=pd.read_csv(r"C:\Users\Divyasri\OneDrive\Desktop\AIML\fires.csv")
data.head()

data.columns

data.drop([124,122,123,168],axis=0,inplace=True)
data.shape

x=data.iloc[ : , :-1].values
y=data.iloc[: ,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy')
model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred))

print(model.predict([[2,	6,	2012,	29,	61,	13,	1.3,	64.4,	4.1,	7.6,	1,	3.9,	0.4,
]]))

sample=pd.read_csv(r"C:\Users\Divyasri\OneDrive\Desktop\AIML\pred.csv")
sample.shape

p=model.predict(sample)

sample['status']=p

sample.to_csv(r"C:\Users\Divyasri\OneDrive\Desktop\AIML\prediction.csv")

