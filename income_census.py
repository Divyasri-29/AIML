# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:29:23 2023

@author: Divyasri
"""

import pandas as pd
names=[]
for i in 'abcdefghijklmno':
    names.append(i)
data=pd.read_csv(r"C:\Users\Divyasri\OneDrive\Desktop\AIML\income.csv",names=names)
data.head()
data.shape

data.isna().sum()

data['b'].value_counts()
data['b']=data['b'].replace(to_replace=' ?',value=' Private')

data['g'].value_counts()
data['g']=data['g'].replace(to_replace=' ?',value=' Prof-specialty')

data['n'].value_counts()
data['n']=data['n'].replace(to_replace=' ?',value=' United-States')

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in 'bdfghijn':
    data[i]=le.fit_transform(data[i])

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy')
model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred))