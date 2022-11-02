# -*- coding: utf-8 -*-
"""ML3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fwCiAf3mpB2-it7pur9TSMD1H_FaDOZz
"""

#25th Oct,2022

#MACHINE LEARNING - SUPERVISED LEARNING  - REGRESSION - LINEAR REGRESSION
#Univariate Linear Regression/Single Linear Regression - One column input and one column output
#Dataset - raw unprocessed data in form of rows and columns
#Dataframe - Tabled data
#Dataset - Area vs Prices
#Dataset - https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/areavsprices.csv
#Area in sqft and Prices is rupees

#1.Take the data and create dataframe
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/areavsprices.csv')
df
#Imaginary Story - Imagine a Real Estate broker/Agent comes to you and gives you the below dataset and says
#create a model for me ,which could predict the property prices based on the data I gave

#2.PRE PROCESSING
#We are not performing step no 2 , due to limited data /Not required

#3.DATA VISUALISATION - CREATING of GRAPHS
import matplotlib.pyplot as plt
#plt.scatter(x-axis,y-axis)
plt.scatter(df['Area'],df['Prices'])
plt.title('Area vs Prices')
plt.xlabel('Area')
plt.ylabel('Prices')

#Input(x) - Area column,output(y) - Prices column

#4.Divide the data into input and output
#Input(x) is always 2 dimensional,output(y) is 1 dimensional array
#.iloc[row slicing,column slicing]
#In column's place,if there is a ':' , then array is 2 dimensional
x = df.iloc[0:6,0:1].values #df.iloc[:,0:1].values
x

#In column place , if there is no ':',then array is 1 dimensional
y = df.iloc[:,1].values #y = df['Prices'].values
y

#Step no 5 , we are not performing/not required

#Step no 6 is not required here

#7.Run a classifier,REGRESSOR or clusterer(Applying a suitable algorithm)
#sklearn.linear_model - package(collection of libraries/modules),LinearRegression - Library name
from sklearn.linear_model import LinearRegression
model = LinearRegression()

#8.FIT the model(Mapping/Plotting the inputs with the outputs)
#LinearRegression.fit(x,y)
model.fit(x,y)#We are plotting the values of x and y inside the LINEARREGRESSION library

#9.Predict the output
y_pred = model.predict(x) #Using the input values, we predict the output
y_pred #PREDICTED OUTPUT VALUES

y #ACTUAL OUTPUT VALUES

#CONCLUSION: We have to compare , y_pred and y.
#SO when we compare ,we come to know that there is a huge difference.
#This huge difference does not mean that my model has predicted wrong.
#It only means that my model is NOT LINEAR/LESS LINEAR.
#LINEARITY of a model depends on the Nature of the data and the size of the data

#INDIVIDUAL PREDICTION
#I want to know the price of 2000 sqft plot
model.predict([[2000]])

#CROSS VERIFY
#y = mx + C #Equation of a straight line
#m - slope
#C -constant/y-intercept
#y - dependant variable
#x - independant variable

m = model.coef_ #slope
m

C = model.intercept_ #y-intercept
C

#y = mx+C
m * 2000 + C

#FINAL VISUALISATION - BEST FIT LINE
plt.scatter(x,y) #Actual OUTPUT VALUES
plt.plot(x,y_pred,c = 'orange')#Predicted output values
plt.title('BEST FIT LINE')
plt.xlabel('Area')
plt.ylabel('Prices')

