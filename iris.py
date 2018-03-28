# Gerhard van der Linde - 27 March 2018
# Student ID: G00364778
# GMIT 52167 Final Project

import functions as f

data = f.read_csv_datafile(r'data/iris.data')
#f.creat_xy_plots(data)
#stat=f.calc_stats(data, screenprint=True)
f.plot_hist(data,action='file')
