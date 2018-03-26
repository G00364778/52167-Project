# Gerhard van der Linde
# Student ID: G00364778
# GMIT 52167 Final Project

"""
https://www.math.umd.edu/~petersd/666/html/iris_pca.html
"""

# 1. sepal length in cm 
# 2. sepal width in cm 
# 3. petal length in cm 
# 4. petal width in cm 
# 5. class: 
# -- Iris datasetosa 
# -- Iris Versicolour 
# -- Iris Virginica

# 6.7,3.0,5.2,2.3,Iris-virginica

import numpy as np
from matplotlib import pyplot as pl
import csv
from sklearn.preprocessing import normalize as norm

with open(r'data\iris.data') as file:
    line=csv.reader(file)
    data=list(line)

data.pop()#pop the empty line from the csv file read
data=np.asarray(data)#create a numpy array to work with
data=data[0::,0:4].astype(float).transpose()#convert all numbers to floats and transpose the dataset
#data_o=np.copy(data)#create a copy before average and normalise for comparison
print('floated and transposed')
print(data[0,0:5])
print(data[1,0:5])
#exit()
#step through the datadataset and subtract the average value from the dataset
for d in range(0,4):#loop through the four datasets
    for i in range(0,101,50): # loop through the 3 types in datasets
        start=i
        stop=i+50
        data[d,start:stop]=data[d,start:stop]+np.median(data[d,start:stop])
print('subrtact mean')
print(data[0,0:5])
print(data[1,0:5])
print('normalised')
#data=norm(data)
print(data[0,0:5])
print(data[1,0:5])
#exit()
x=0
y=3
dataset=data_o
pl.plot(dataset[x,0:50],dataset[y,0:50],'ro',dataset[x,50:100],dataset[y,50:100],'go',dataset[x,100:150],dataset[y,100:150],'bo')
pl.savefig(r'pl1.jpg')
pl.close()
dataset=data
pl.plot(dataset[x,0:50],dataset[y,0:50],'ro',dataset[x,50:100],dataset[y,50:100],'go',dataset[x,100:150],dataset[y,100:150],'bo')
pl.savefig(r'pl2.jpg')
pl.close()
