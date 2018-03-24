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
# -- Iris Setosa 
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
data=data[0::,0:4].astype(float).transpose()#convert all numbers to floats and transpose the set
#print(data)
data_n=norm(data-np.mean(data))
x=0
y=3
set=data
pl.plot(set[x,0:50],set[y,0:50],'ro',set[x,50:100],set[y,50:100],'go',set[x,100:150],set[y,100:150],'bo')
pl.savefig('pl1.jpg')
pl.close()
set=data_n
pl.plot(set[x,0:50],set[y,0:50],'ro',set[x,50:100],set[y,50:100],'go',set[x,100:150],set[y,100:150],'bo')
pl.savefig('pl2.jpg')
pl.close()
