# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:13:48 2018

@author: Moaz Magdy
"""
import numpy as np
import matplotlib.pyplot as plt

#Simple Linear regression without using matrices

# y = mx + b
# m = theta1, b = theta0


def cal_error(m,b,points): #Difference between labels and predictions
        totalerr = np.zeros(len(points))
        for i in range(len(points)):
            x = points[i,0]
            y = points[i,1]
            totalerr[i] = (y - ((m*x) + b))**2
        return sum(totalerr)/(float(len(points)))
    
def gradient_descent(learning_rate,num_iterations,initial_m,initial_b,points):
        N = len(points)
        plt.scatter(points[:,0], points[:,1])
        plt.show()
        updated_b = initial_b
        updated_m = initial_m
        for j in range(num_iterations):
            temp_b = 0
            temp_m = 0
            for i in range(0, len(points)):
                x = points[i,0]
                y = points[i,1]
                temp_b += -(2/N) * (y - ((initial_m * x) + initial_b))        # += To sum all values sequentially 
                temp_m += -(2/N) * (y - ((initial_m * x) + initial_b)) * x
            updated_b = initial_b - (learning_rate * temp_b)
            updated_m = initial_m - (learning_rate * temp_m)
            initial_m = updated_m
            initial_b = updated_b
        return [updated_b, updated_m]
  
def run():
     points = np.loadtxt('C:\ex1data1.txt',delimiter=',')
     learning_rate = 0.0001
     num_iterations = 1000
     initial_m = 0
     initial_b = 0
     [b, m] = gradient_descent(learning_rate,num_iterations,initial_m,initial_b,points)
     print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations,b,m,cal_error(m,b,points)))

if __name__ == "__main__":
    run()    
    
