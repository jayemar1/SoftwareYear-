# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:00:17 2020

@author: 612734775
"""

#Imports all the modules that allows me to mangage the data how I would like using their unique properties
#'plt', 'pd' and 'np' names are given to their respective module for ease of use

import csv
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt



#Calls on the selected file
# The instruction to open and read the file is given a new name
with open('data1.csv') as data:

    #A variable that stores the 'reader' method with csv file instructions as an argument
    readFile = csv.DictReader(data)
    
    #Variable for the counter function
    speedCount = Counter()
    
    #loops through all data in csv file
    #updates the counter with the data for speed
    for row in readFile:
        speedCount.update(row['00'].split(','))

#Arrays for the data to be stored        
speed = []
carsTravellingAtThatSpeed = []

#Only displays the 10 most common recorded speeds using the 'most_common' method
#Joins items to their relevant variables
for item in speedCount.most_common(10):
    speed.append(item[0])
    carsTravellingAtThatSpeed.append(item[1]) 


#Creates bar graph and plots data on x and y axis   
plt.bar(speed, carsTravellingAtThatSpeed)

#Add title to graph
plt.title('Top 10 speeds recorded by 200 cars')

#Adds a label to the x-axis
plt.xlabel('Speed in mph')

#Adds a label to the y-axis
plt.ylabel('Number of cars travelling at X speed')

#Adds a black background to the graph
plt.style.use('dark_background')

#Adds grid to graph
plt.grid()

#Displays the graph
plt.show()

#Analysis of data

#Variable that uses pandas to read the csv file
calc = pd.read_csv ('data1.csv')

#Calculates average
average = calc['00'].mean()
print("The avarage speed is: ",average)

#Calculates median
showMedian = calc['00'].median() 
print("The median speed is: ",showMedian)

#Calculates standard deviation 
sd = calc['00'].std() 
print("The standard deviation of the speed is: ",sd)

#Calculates sum 
showSum = calc['00'].sum() 
print("The sum of the speed is: ",showSum)

#Calculates variation 
showsVariation = calc['00'].var() 
print("The variation of the speed is: ",showsVariation)


















