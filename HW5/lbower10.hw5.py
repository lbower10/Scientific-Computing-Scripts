#!/usr/bin/env python3
'''
	File: lbower10.hw5.py
	Author: Logan Bowers
	NetID: lbower10
	COSC 370 Homework 5
'''

### Problem 17 (use log-log scale) ###
from cubicSpline import *
from numpy import array,log10
xData = array([0.2, 2.0, 20.0, 200.0, 2000.0, 20000.0])
yData = array([103.0, 13.9, 2.72, 0.8, 0.401, 0.433])
Re_array= array([5.0, 50.0, 500.0, 5000.0])
logxData = log10(xData)
logyData = log10(yData)
k = curvatures(logxData, logyData)

# loop to eval the Cubic Spline for elements in Re_array at logscale
print('\nInterpolating for drag coefficients (C_D)...\n    Re\tC_D')
for Re in Re_array:
	logy = evalSpline(logxData, logyData, k, log10(Re))
	print('{:6.1f}\t{:5.3f}'.format(Re,10.0**logy))

### Problem 19 (do not use log-log scale) ###
tData = array([0.0, 21.1, 37.8, 54.4, 71.1, 87.8, 100.0])
mData = array([1.79, 1.13, 0.696, 0.519, 0.338, 0.321, 0.296]) 
T_array = array([10.0, 30.0, 60.0, 90.0])
k = curvatures(tData, mData)

# Create loop to evaluate the Cubic Spline for the elements in the T_array
print('\nInterpolating for kinematic viscosity (CMu_k)...\n    T\tMu_k')
for temp in T_array:
	y = evalSpline(tData, mData, k, temp)
	print('{:6.1f}\t{:5.3f}'.format(temp,y))