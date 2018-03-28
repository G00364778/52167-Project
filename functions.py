# Gerhard van der Linde - 22 March 2018
# Student ID: G00364778
# GMIT 52167 Final Project

"""
The purpose of this python code is to perform three major functions on the iris dataset

    * Read is the csv data from a text file and return it in a format for further processing
    * Run some basic statistical calculations on the dataset
    * Graph the results for graphical comparison 

The raw iris dataset consists of the following

1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
    - Iris Setosa 
    - Iris Versicolour 
    - Iris Virginica

The csv read returns this sampe: # 6.7,3.0,5.2,2.3,Iris-virginica

"""
import numpy as np
from matplotlib import pyplot as pl
import csv
# from sklearn.preprocessing import normalize as norm # not used, but kep for reference
import os
from scipy import stats

setnames=['sepl','sepw','petl','petw']
setlabels=['Sepal Length','Sepal Width','Petal Length','Petal Width']
species=['Setosa','Versicolour','Virginica']
statlabels=['nobs', 'min', 'max', 'mean', 'var', 'skew', 'kurt']


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

    data.pop() # pop the empty line from the csv file read
    data=np.asarray(data) #c reate a numpy array to work with
    data=data[0::,0:4].astype(float).transpose() # convert all numbers to floats and transpose the data
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
    #print(b) # [0, 50, 100, 150] # test the calculations
    for x in range(cols): # loop through the four datasets
        for y in range(x,cols):
            if x!=y:
                #print(x,y)
                Set,Ver,Vir=pl.plot(dataset[x,b[0]:b[1]],dataset[y,b[0]:b[1]],'ro',dataset[x,b[1]:b[2]],dataset[y,b[1]:b[2]],'go',dataset[x,b[2]:b[3]],dataset[y,b[2]:b[3]],'bo')
                pl.title('Iris plot by species - {} x {}'.format(setlabels[x],setlabels[y]))
                pl.legend((Set,Ver,Vir),species)
                pl.xlabel('{}(cm)'.format(setlabels[x]))
                pl.ylabel('{}(cm)'.format(setlabels[y]))
                filename='plots\\iris_plt_{}_{}.png'.format(setnames[x],setnames[y])
                os.makedirs(os.path.dirname(filename),mode=0o777,exist_ok=True)
                pl.savefig(filename)
                pl.close()

def calc_stats (data, screenprint=False):
    """
    Create a list of statistcis and create an array with the results sorted by return types
    with the option to print them out in a table.
    
    Imputs: data - the set returned by read_csv_datafile

    Outputs:
        nobs - number of objects in set
        min  - the minimum values in the set
        max  - the maximum values in the set
        mean - the mean(average) of the set
        var  - the variance or standard deviation in the set
        skew - the skewness indicating the lack of symmetry, symmetric if it looks the same to the left and right of the center point
        kurt - the kurtosis, heavy-tailed or light-tailed
    """
    cols,samples=np.shape(data) # retrieve the columns and samples from the set passed in
    stat=[]
    vals=[]
    for i in range(cols):
        stat.append(stats.describe(data[i])) # collect the stats
    #myarr=np.asarray(stat)
    statArr=[]
    for i in range(cols):
        #print
        nobsv, minmaxv, meanv, variancev, skewv, kurtosisv = stat[i]
        minv,maxv=minmaxv
        vals=nobsv, minv, maxv, meanv, variancev, skewv, kurtosisv
        statArr.append(vals)
        #print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(nobsv, minv, maxv, meanv, variancev, skewv, kurtosisv),sep='',end='')
    st=np.asarray(statArr).transpose()
    if screenprint==True:
        #print the headings
        print('\n+-------+---------------+---------------+---------------+---------------+')
        print('|Stat',end='')
        for i in range (len(setlabels)):
            print('\t|{}'.format(setlabels[i]),sep='', end='')
        print('\t|\n',end='')
        print('+-------+---------------+---------------+---------------+---------------+')
        row,col=np.shape(st)
        # print the data
        for i in range(row):
            print('|{}\t'.format(statlabels[i]),sep='',end='')
            for j in range(col):
                print('|{:7.3f}\t'.format(st[i][j]),sep='',end='')
            print('|\n',end='')
        print('+-------+---------------+---------------+---------------+---------------+')
    return st

def plot_hist(data,action='view'): # pass view of save for actions
    for i in range(len(data)):
        pl.hist(data[i])
        pl.ylabel(setlabels[i])
        if action == 'view':
            pl.show()
        elif action == 'save':
            filename='plots\\iris_hist_{}.png'.format(setnames[i])
            os.makedirs(os.path.dirname(filename),mode=0o777,exist_ok=True)
            pl.savefig(filename)
            pl.close()

data=read_csv_datafile()
#creat_xy_plots(data)
#stat=calc_stats(data, screenprint=True)
plot_hist(data,action='save')
