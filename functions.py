# Gerhard van der Linde
# Student ID: G00364778
# GMIT 52167 Final Project

"""

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
# 6.3,2.5,5.0,1.9,Iris-virginica
# 6.5,3.0,5.2,2.0,Iris-virginica
# 6.2,3.4,5.4,2.3,Iris-virginica
# 5.9,3.0,5.1,1.8,Iris-virginica

import numpy as np

def makefloat(teststr):
    """
    Convert strings containing numbers into floatingpoint values,otherwise return the string as is.
    
    return 
        a tring
        or a float
    """
    try:
        return float(teststr) # return a floating point value if possibe.
    except:
        return teststr # otherwise return the string as is


with open(r'data\iris.data') as file:
    datArr=[]
    for line in file:
        data=line.strip().split(',') # strip the newlines and spaces from the line and split on commas
        data = [makefloat(i) for i in data] # convert the number strings to floating point values
        if len(data)>1: # check for empty lines and skip
            #print(data,len(data))
            datArr.append(data)

npDat=np.asarray(datArr)
np.sp
print(npDat)


