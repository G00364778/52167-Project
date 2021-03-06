<!-- https://guides.github.com/features/mastering-markdown/ -->

# 52167-Project

GMIT Programming and scripting project 2018

[Project description document](doc/GMIT_Project_Description.pdf)

## To be completed

- [x] Research background information about the data set and write a summary about it.
- [x] Keep a list of references you used in completing the project.
- [x] Download the data set and write some Python code to investigate it.
- [x] Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set. A Python script will quickly do this for you.
- [x] Write a summary of your investigations.
- [x] Include supporting tables and graphics as you deem necessary.

## Background information on the Iris data set

![Iris Setosa Sample](http://www.twofrog.com/images/iris38a.jpg)

There seems to be vast amounts of information on the topic(About 5,230,000 results on google) of the iris data set and several studies and papers derived around the subject and used as examples to explain statistics and statistical analyses of data sets.

The raw data set is available from various sources online but the main set for this exercise was obtained from University of California's Machine Learning repository cited in the list of references below.

The data set consists of 150 instances of three classes with 4 attributes for every class.

Attribute Information:

1. sepal length in cm
1. sepal width in cm
1. petal length in cm
1. petal width in cm
1. class:
   1. Iris Setosa
   1. Iris Versicolour
   1. Iris Virginica

In order to be effective in deriving a meaning conclusion or perform any kind of analyses on the data, one needs to clarify the values recorded in the set, so basically understand what sepal and a petal is.

![Petal and Sepal](https://www.wpclipart.com/plants/diagrams/plant_parts/petal_sepal_label.png)

So a petal is the obvious that most of us know from regular flowers and the sepal is the more rigid typically stem coloured part of the flower supporting the petals. In Iris flowers this is more confusing as sepals tends to look like petals being a similar colour, however they would be behind petals performing the function of sepals.

## Investigating the data set

### Graphing the data

A Mat lab paper published by D Peters(referenced) suggested normalising the data sets for improved results.

Samples from this process yielded the following:

Original set - floated and transposed

```python
[ 5.1  4.9  4.7  4.6  5. ]
[ 3.5  3.   3.2  3.1  3.6]
```

Subtract mean of subsets by species

```python
[ 0.094 -0.106 -0.306 -0.406 -0.006]
[ 0.082 -0.418 -0.218 -0.318  0.182]
```

Normalise the entire set

```python
[ 0.01506051 -0.01698312 -0.04902675 -0.06504857 -0.00096131]
[ 0.01986748 -0.10127569 -0.05281842 -0.07704706  0.04409611]
```

The result of the normalisation process eliminated all the separations in the sets. Another idea was calculating the products of the length and width results in order to evaluate separation, however no better results were produced as seen in the single set parameters.

The next stage was to produce all the possible scatter plots colour coded by species. This yielded the most satisfactory results and created a reasonably good separation on most plots.

![Scatter Plots](samples/Capture.JPG)
See the [plots folder](plots/) for full size samples.

The best sets were produced by:

- Sepal Length x Sepal width with a 96% separation in the overlapping species
- Sepal Length x Petal width with a 94% separation in the overlapping species

### Analysing the data sets

Reviewing the data sets through statistical analyses a very handy library and feature was found in [SciPy][1].stats function. A single function call wraps all the handy statistics into a single function call.

Statistic|Sepal Length|Sepal Width|Petal Length|Petal Width
---------|:----------:|:---------:|:----------:|:-----------:
**nobs**|150.000|150.000|150.000|150.000
**min**|4.300|2.000|1.000|0.100
**max**|7.900|4.400|6.900|2.500
**mean**|5.843|3.054|3.759|1.199
**variance**|0.686|0.188|3.113|0.582
**skewness**|0.312|0.331|-0.272|-0.104
**kurtosis**|-0.574|0.241|-1.395|-1.335

- nobs  - number of objects in set
- min   - the minimum values in the set
- max   - the maximum values in the set
- mean  - the mean(average) of the set
- var   - the variance or standard deviation in the set
- skew  - the skewness indicating the lack of symmetry, symmetric if it looks the same to the left and right of the centre point.
- kurt  - the kurtosis is a measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution.

So from the results in the analyses it seems to suggest that the data sets are well within the boundaries of analyses and do not require normalisation and should produce meaningful results.

[Some further reading suggested that histograms are in fact a very good tool for visualising a statistical data set][5]. Python PyPlot library offers a very easy way to produce histograms in a single line of code:

```python
pl.hist(data[i])
```

The following histograms were completed and personally makes more sense than trying to make meaningful deductions from a set of statistical values in a data set.

![Histogram Samples](samples/Histograms.jpg)

So the aim was to look at the histograms derived from the data sets, using the [Wikipedia examples][6] as references, and predict what data set will produce the best results in separation of species on x-y plots. Symmetric, unimodal plots seem to produce the worst results and it seems like symmetric plots is the ideal. Five of the six [x-y scatter plots][4] produced acceptable separations on the plots. The only set mixed up completely is "sepel length" x "sepal width". Both these plots appear very symmetric and unimodal.

### Skewness and Kurtoses

Skewness is a measure of symmetry, or more precisely, the lack of symmetry. A distribution, or data set, is symmetric if it looks the same to the left and right of the centre point.

Kurtosis is a measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution. That is, data sets with high kurtosis tend to have heavy tails, or outliers. Data sets with low kurtosis tend to have light tails, or lack of outliers. A uniform distribution would be the extreme case.

## Using Python as a tool for data analyses

The python code used in this exercise in contained in the GitHub repository as [functions.py][2] The three functions developed for this exercise are:

- read_csv_datafile(datafile='data\\iris.data')
- calc_stats(data, screenprint=False)
- creat_xy_plots(data set, species_in_set=3)

The functions are called from the [iris.py][3] code to execute the three functions.

```python
import functions as f

data = f.read_csv_datafile(r'data/iris.data')
f.creat_xy_plots(data)
stat=f.calc_stats(data, screenprint=True)
```

The first functions reads the csv data and returns in in numpy array format ready for pyplot graphing and numpy or scipy statistical analyses libraries.

The second function generates x,y scatter plots and stores them in the [plots][4] sub-folder

## List of references

1. [Wikipedia - Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
1. [Iris Setosa - classification details](https://alchetron.com/Iris-setosa)
1. [Sir Ronal Fisher - British statistician and geneticist](https://en.wikipedia.org/wiki/Ronald_Fisher)
1. [Iris data set](https://archive.ics.uci.edu/ml/datasets/iris) from the UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.
1. [Example for Principal Component Analysis (PCA): Iris data](https://www.math.umd.edu/~petersd/666/html/iris_pca.html)
1. [Statistical methods](https://www.encyclopedia.com/computing/dictionaries-thesauruses-pictures-and-press-releases/statistical-methods)
1. [Skewness and Kurtosis](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm)
1. [Kurtosis](https://en.wikipedia.org/wiki/Kurtosis)
1. [SciPy Statistical reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.describe.html)
1. [Interpretation of statistical data](https://blog.udemy.com/interpretation-of-data/)
1. [Parametric and Non-parametric tests for comparing two or more groups](https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1b-statistical-methods/parametric-nonparametric-tests)
1. [Using histograms to graphically summarise distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm)
1. [Histograms on Wikipedia](https://en.wikipedia.org/wiki/Histogram)

[1]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.describe.html
[2]: functions.py
[3]: iris.ph
[4]: /plots
[5]: https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm
[6]: https://en.wikipedia.org/wiki/Histogram#Examples