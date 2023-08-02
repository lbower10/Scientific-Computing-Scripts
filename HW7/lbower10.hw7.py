#!/usr/bin/env python3
'''
    Logan Bowers --- lbower10
    COSC 370 HW7
    R - Radial distance from center of Earth to satellite
    Theta - Satellite's angle at its location in orbit
    C - Constant in equation
    e - Eccentricity of orbit, descripes orbital shape
    Alpha - Phase angle/angular shift of orbit
 '''

from newtonRaphson2 import *
from math import sin, pi
import numpy as np
import matplotlib.pyplot as plt

#  Complete the following function below, where F[j] returns the left-hand-side
#  of [Eqn1] where R and theta are given by the jth data pair.
def F(x):
    # from original comments (I removed them because they drove me crazy)
    R, theta = np.array([6870, 6728, 6615]), np.array([-30, 0, 30]) * (pi / 180)
    F = zeros((len(x)), dtype=float64)
    for i in range(len(R)):
        F[i] = R[i] - x[0] / (1 + x[1] * sin(theta[i] + x[2]))
    
    return F

# Initial guess
x = np.array([6800, 0.5, 0])

# Complete the call to the N-R method to solve for unknowns
x = newtonRaphson2(F, x)

# Print the solution vector x from N-R
print()
np.set_printoptions(precision = 3)
print('[ C  e  alpha] = ' + np.array_str(x))

# Calculate minimum trajectory and angle using components of x
minTheta = (pi / 2 - x[2]) * (180 / pi) # pi/2 - alpha in degrees
minR = x[0] / (1 + x[1] * sin((minTheta * (pi/180)) + x[2]))

# Print minimum trajectory results
print('Minimum trajectory = %.3f km' % minR)
print('Angle at which minimum trajectory occurs = %.3f degrees' % minTheta)
print()

#-------------------------------------------------------------
# Outputs for verification:
# C  e  alpha] = [  6.819e+03   4.060e-02   3.408e-01]
# Minimum trajectory = 6553.239 km
# Angle at which minimum trajectory occurs = 70.475 degrees
#-------------------------------------------------------------

# Create arrays of points spaced every 0.01 radians around the satellite orbit
# (theta) and their respective trajectories (R)

theta = np.arange(0, 2*pi, 0.01) # theta and R are arrays now
R = x[0] / (1 + x[1]*np.sin(theta + x[2]))

# Plot orbit and minimum trajectory point

ax = plt.subplot(111, polar = True)
ax.plot(theta, R, color = 'r', linewidth = 2, label = 'Path')
ax.plot(minTheta, minR, 'bo', label = 'Min')
ax.legend(numpoints = 1)
ax.grid(True)
ax.set_title("Satellite path")
plt.show()