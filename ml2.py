# -*- coding: utf-8 -*-
"""ML2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17MMifpo2rmirQLbaOZS2ITLwISWeZeTZ
"""

#.ipynb - .Interactive Python Notebook
#.py - .Python
#To execute a cell - Ctrl + enter,Shift + enter,Alt + enter

#Hi there

print()

print('Hello World')

print("Hello World")

#variable - a named memory location
a = 25

print(a)

a

#PYTHON LIBRARIES - collection of modules
#NUMPY,MATPLOTLIB,PANDAS,SKLEARN,OPENCV

#NUMPY - Numerical Python
#Numpy is used instead of a list
#Numpy is much more faster and efficient ,when compared to a list
#Numpy is always an array

import numpy as np
a = np.array(1)
a

type(a)

a.ndim #It tells us the dimension of the array - 0 dimensional

a.size #tells us the total number of elements in the array

b = np.array([1,2,3,4,5])
b

b.ndim # 1 dimensional

b.size

c = np.array([[1,2,3],[4,5,6]])
c

c.ndim # 2 dimensional

c.size # 6 elements in c

#2.MATPLOTLIB - VISUALISATION LIBRARY(GRAPHS or REPRESENTATIONs)

#1.LINE GRAPH/PLOT using LISTS
import matplotlib.pyplot as plt
a = [1,2,3,4]
b = [5,6,7,8]
#plt.plot(x-axis,y-axis)
plt.plot(a,b,color = 'lime',marker = '*',linewidth = 5)
plt.title('LINE PLOT')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

#LINE GRAPH using numpy array
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
plt.plot(x,y,marker = '*',color = 'lime')
plt.title('LINE PLOT')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.xticks(range(0,30,2))

#2.SCATTER PLOT
a = [1,2,3,4,5]
b = [6,7,8,9,10]
plt.scatter(a,b,color = ['gold','red','lime','b','k'])
plt.title('SCATTER PLOT')
plt.plot(a,b)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

#3.BAR GRAPH
names = ['Akshay','Dheeraj','John','Mac']
weight = [58,86,78,69]
plt.bar(names,weight,color = ['Red','Orange','Lime','gold'])
#change plt.bar to plt.barh for horizontal bars
plt.title('Bar Graph')
plt.xlabel('Names')
plt.ylabel('Weight')

#3.PANDAS - It is used to create Series and Dataframe.
#Series - column
#Dataframe - Tabled data(data in form of a table)

mydataset = {'cars':['BMW','Volvo','Ford'],'passings':[3,7,2]}
mydataset

type(mydataset)

#Let us create a dataframe using this dictionary
import pandas as pd
df = pd.DataFrame(mydataset)
df

type(df)

a = [1,7,2,6]
myvar1 = pd.Series(a)
myvar1

type(myvar1)

#EXPLORATORY DATA ANALYSIS - PRE MACHINE LEARNING
#We find insights,we come to conclusions and we explore our data
#dataset - collection of raw data in form of rows and columns
#dataset - https://storage.googleapis.com/kagglesdsdata/datasets/9590/13660/fruit_data_with_colors.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221018%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221018T131659Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=38eafc5e8b324a3c011a319acb446a03e654794f200133b1f4830e397ea44da77b3684afd590879189702bad3f86c52d77a8888cc83ef26ee26336e443954874399613bbaa8b13ee00beee08ac33425254b7e199bc242823947ccfedbfca8874c4cb04d8cf9bcff768b6787a5f9ae7d8402ef5cedcee79d0b7d8f9cc6984167490b4f9809fa315a9fb892a612101c311bc77766815e4159d0489d0a9087634c4d47c72d0d68340fe6d73715e0509357100748f0352a83bf0da34ac1d0f77aff23947c1f4bbb903b587fd8a9a9a5790f1a68e9e6bd8ef24804122098892a98ba2be69bf53c73f1f62e1b2dd559bbf8eccce70b9929601dd70b954323a0b72cc75

#Take the data and create dataframe
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/kagglesdsdata/datasets/9590/13660/fruit_data_with_colors.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221018%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221018T131659Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=38eafc5e8b324a3c011a319acb446a03e654794f200133b1f4830e397ea44da77b3684afd590879189702bad3f86c52d77a8888cc83ef26ee26336e443954874399613bbaa8b13ee00beee08ac33425254b7e199bc242823947ccfedbfca8874c4cb04d8cf9bcff768b6787a5f9ae7d8402ef5cedcee79d0b7d8f9cc6984167490b4f9809fa315a9fb892a612101c311bc77766815e4159d0489d0a9087634c4d47c72d0d68340fe6d73715e0509357100748f0352a83bf0da34ac1d0f77aff23947c1f4bbb903b587fd8a9a9a5790f1a68e9e6bd8ef24804122098892a98ba2be69bf53c73f1f62e1b2dd559bbf8eccce70b9929601dd70b954323a0b72cc75",sep = '\t')
df

df.info() #Tells us the information about our dataframe

df.shape # 59 rows 7 columns

df.size #total number of elements in df

#Slicing
#Slice row indexes from 25 to 43
#df[inclusive:exclusive]
df[25:44]

#Slice row indexes from 25 to 43
#and column indexes 0 and 1
#df.iloc[row slicing,column slicing]
df.iloc[25:44,0:2]

#I just want to know the number of unique fruits(4 from manual count)
df.fruit_name.nunique()

df['fruit_name'].nunique()

#Now I want the unique fruit names
df['fruit_name'].unique()

#Now I want the exact count of each and every fruit
#Apple -19
#Mandarin -5
#Orange - 19
#Lemon - 16
df.groupby('fruit_name').size()

