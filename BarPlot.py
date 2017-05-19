from numpy import *
import random
import matplotlib.pyplot as plt; plt.rcdefaults()
import sys
import math as m
import pylab as p



"""
Simple demo of a horizontal bar chart.
"""
def HorizontalBarChart(people, performance, title, xlabel, ylabel):
	
	y_pos = arange(len(people))+0.5
	
	plt.barh(y_pos, performance, align='center', color = 'g',alpha=0.4)
	plt.yticks(y_pos, people, fontsize = 8, fontweight = 'bold')
	plt.xlabel(xlabel, fontsize = 12, fontweight = 'bold' )
	plt.ylabel(ylabel, fontsize = 12, fontweight = 'bold')
	plt.title(title)

	plt.show()
