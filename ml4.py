# -*- coding: utf-8 -*-
"""ML4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PKufhGOTxMlP5DMY9fy2Y0c-dSfgmVzA
"""

#CLASSIFICATION - LOGISTIC REGRESSION - SUPERVISED LEARNING
#Ex - Purchased or Not Purchased,Yes or No,Fit or Not Fit,Car or Bike,Dog or Cat,1 or 2 or 3
#Dataset - https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/IRIS.csv

#1.Take the data and create dataframe
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/IRIS.csv')
df

#Input - Sepal len,sepal width,petal length and petal width
#Species - output

#2.Step no 2 is not required

#3.step no 3 is also not required for now

#4.Divide the data into i/p and o/p
#input(x) is always 2 dimensional
#output(y) is always 1 dimensional
#df.iloc[row slicing,column slicing]
#In column's place if there is a ':', then array is 2 dimensional
x = df.iloc[:,0:4].values
y = df.iloc[:,4].values #In column's place if there is no ':',then array is 1 dimensional

#5.Train and test variables- If you have more data ,perform step no 5 better accuracy
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 0)

#the variable names can change , but the variable order cannot change

#After train_test_split
#75% of data in x goes to x_train,rest 25% goes to x_test
#75% of data in y goes to y_train,rest 25% goes to y_test

print(x.shape) # 100 %
print(x_train.shape) #75%
print(x_test.shape) #25%

print(y.shape) - 100%
print(y_train.shape) - 75%
print(y_test.shape) - 25%

#6.We are not performing step no 6

#7.Run a CLASSIFIER,Regressor or Clusterer
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#8.Fit the model
#LogisticRegression.fit(x_train,y_train)
model.fit(x_train,y_train)#to train my model , we need i/p training and well as o/p training data

#9.PREDICT THE OUTPUT
y_pred = model.predict(x_test)#using the input testing values , we predict the output
y_pred #PREDICTED OUTPUT VALUES

y_test #ACTUAL OUTPUT VALUES

#10.Accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_pred,y_test)*100

#INDIVIDUAL PREDICTION
model.predict([[5.1,3.5,1.4,0.2]])

model.predict([[5.9,3.0,4.2,1.5]])

model.predict([[7.7,3.0,6.1,2.3]])

#own values
model.predict([[2.5,3.6,5.5,4.5]])

#MAJOR PROJECT
#If you want you can do your major project individually or you can do it in a group of 2 to 3 members.