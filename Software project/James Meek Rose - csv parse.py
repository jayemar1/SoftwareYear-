# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:09:20 2020

@author: James Meek Rose
"""
#Imports all the modules that allows me to mangage the data how I would like using their unique properties
#'plt' and 'np' names are given to their respective module for ease of use

import csv
import matplotlib.pyplot as plt
import numpy as np

#Calls on file called 'Growth.csv'
# 'r' means read, so the programme is instructed to read the file
# The instruction to open and read the file is given the name growth

with open('Growth.csv', 'r') as growth:

    #A variable that stores the 'reader' method with csv file instructions as an argument
    readFile = csv.reader(growth)
    
   #Loops over all the lines in the 'readFile' variable and prints out each line of the list in the console
    for line in readFile:
        print(line)
 
#Unpacks the values of the file 'Growth.csv' into x and y values
# Delimeter is what separates the values in the chosen file
        
x,y = np.loadtxt('Growth.csv', unpack = True, delimiter = ',')

plt.plot(x,y)

#Add title to graph
plt.title('Increase in height with age')

#Adds a label to the x-axis
plt.xlabel('Age in years')

#Adds a label to the y-axis
plt.ylabel('Height in centimeters')

#Adds the indiviual plots to the graph in black, increasing the size and changing the shape to a star
plt.scatter(x, y, color = 'k', s=500, marker = "*" )

#Displays the graph
plt.show()

