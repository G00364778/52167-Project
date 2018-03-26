# Gerhard van der Linde
# Student ID: G00364778
# GMIT 52167 Final Project

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
"""
import numpy as np
from matplotlib import pyplot as pl
import csv
from sklearn.preprocessing import normalize as norm
import os
from scipy import stats

setnames=['sepl','sepw','petl','petw']
setlabels=['Sepal Length','Sepal Width','Petal Length','Petal Width']
species=['Setosa','Versicolour','Virginica']

def read_csv_datafile(datafile=r'data\iris.data'):
    """
    Read the csv data file passed in to the fucntion, parse the data values from the file,
    create a numpy array of floats and transpose them to a format useable in further statistical 
    processing and graphing in array format.

    return value - numpy array of 4 x 50 floatingpoint values
    """
    with open(datafile) as file:
        line=csv.reader(file)
        data=list(line)

    data.pop()#pop the empty line from the csv file read
    data=np.asarray(data)#create a numpy array to work with
    data=data[0::,0:4].astype(float).transpose()#convert all numbers to floats and transpose the data
    return data

def creat_xy_plots(dataset, species_in_set=3):
    """
    Create a plot from the dataset passed in. 

    Imputs: dataset - the numpy array with sampe data retrieved in 'read_csv_datafile'
            specied in set - default of 3 onless specified

    Outputs: generating plot images in the 'plots' subfolder
    """
    cols,samples=np.shape(dataset) # retrieve the columns and samples from the set passed in
    b=[i for i in range(0,(samples+(samples//species_in_set)),(samples//species_in_set))] # calculate boundaries
    #print(b) # [0, 50, 100, 150]
    for x in range(cols):
        for y in range(x,cols):
            if x!=y:
                #print(x,y)
                Set,Ver,Vir=pl.plot(dataset[x,b[0]:b[1]],data[y,b[0]:b[1]],'ro',dataset[x,b[1]:b[2]],dataset[y,b[1]:b[2]],'go',dataset[x,b[2]:b[3]],dataset[y,b[2]:b[3]],'bo')
                pl.title('Iris plot by species - {} x {}'.format(setlabels[x],setlabels[y]))
                pl.legend((Set,Ver,Vir),species)
                pl.xlabel('{}(cm)'.format(setlabels[x]))
                pl.ylabel('{}(cm)'.format(setlabels[y]))
                filename='plots\\iris_plt_{}_{}.png'.format(setnames[x],setnames[y])
                os.makedirs(os.path.dirname(filename),mode=0o777,exist_ok=True)
                pl.savefig(filename)
                pl.close()

data=read_csv_datafile()
#creat_xy_plots(data)

cols,samples=np.shape(data) # retrieve the columns and samples from the set passed in
stat=[]

for i in range(cols):
    stat.append(stats.describe(data[i]))#collect the stats
for i in range (len(setlabels)):
    print('\t|{}'.format(setlabels[i]),sep='', end='')
print('\n')
#myarr=np.asarray(stat)
for i in range(cols):
    #print
    nobsv, minmaxv, meanv, variancev, skewv, kurtosisv = stat[i]
    minv,maxv=minmaxv
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(nobsv, minv, maxv, meanv, variancev, skewv, kurtosisv),sep='',end='')


