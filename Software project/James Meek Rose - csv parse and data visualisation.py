# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:00:17 2020

@author: 612734775
"""

#Imports all the modules that allows me to mangage the data how I would like using their unique properties
#'plt' and 'np' names are given to their respective module for ease of use

import csv
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


#Calls on the selected file
# The instruction to open and read the file is given a new name
with open('data1.csv') as data:

    #A variable that stores the 'reader' method with csv file instructions as an argument
    readFile = csv.DictReader(data)
    
   
    speedCount = Counter()
    
    for row in readFile:
        speedCount.update(row['00'].split(','))
        
speed = []
carsTravellingAtThatSpeed = []

for item in speedCount.most_common(10):
    speed.append(item[0])
    carsTravellingAtThatSpeed.append(item[1]) 
    
plt.bar(speed, carsTravellingAtThatSpeed)




#Add title to graph
plt.title('Top 10 speeds recorded by 200 cars')

#Adds a label to the x-axis
plt.xlabel('Speed in mph')

#Adds a label to the y-axis
plt.ylabel('Number of cars travelling at X speed')

#Adds a black background to the graph
plt.style.use('dark_background')

plt.grid()

#Displays the graph
plt.show()


    
