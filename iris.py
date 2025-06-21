import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   #importing the packages

data=pd.read_csv(r"C:\Users\Divyasri\Desktop\AIML\iris.csv") #raeding the csv file.
print(data.head()) #printing the first five rows.
 
#data=data.fillna(1.2)
data.dropna(inplace=True) #deleting the empty spaces

x=np.array(data.iloc[:,:-1])# converting dataframe into array.
y=data.iloc[:,-1].values  #dividing into independent features and target features
print(x)

from sklearn.model_selection import train_test_split # we are dividing into training and testing 
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=9)#giving 20% to the testing.

from sklearn.neighbors import KNeighborsClassifier #importing the algorithm
model=KNeighborsClassifier(n_neighbors=3) # keeping the k value as 3

model.fit(xtrain,ytrain) # training the data

ypred=model.predict(xtest) # predicting the output of xtest and storing in ypred

from sklearn.metrics import accuracy_score 
print(accuracy_score(ytest,ypred)*100) # comparing the ypred and ytest.








