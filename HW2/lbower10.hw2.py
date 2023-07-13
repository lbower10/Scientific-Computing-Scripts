#!/usr/bin/env python3
####################################################################

'''
	File: lbower10.hw2.py
	Author: Logan Bowers
	NetID: lbower10
	Class: COSC 370
	Date 7/10/23
'''

from numpy import zeros, ones, array, float64, inf
from numpy import linalg
from LUdecomp import *

norm = linalg.norm
TOL = 1e-6 # suggestion from writeup
err = 0
n = 0
while err < TOL:
	n+=1
	a = zeros((n,n),dtype=float64)
	b = zeros((n),dtype=float64)
	soln = ones((n), dtype=float64) # The correct solution is all 1's

  # Use the loops below to define the matrix 'a' and vector 'b':
	for i in range(n):
		for j in range(n):
			a[i,j] = 1/(i + j + 1) # hilbert matrix
			b[i] += a[i,j] # b_i = sum from j = 1 to n of A_ij


	# Call appropriate functions from the LUdecomp.py module to
	# solve the equations A x = b with the b-vector being overridden
	# by the solution vector x.
	a = LUdecomp(a)
	b = LUsolve(a, b)

	# Your solution should be stored in 'b' (if you used a 
	#  different variable name, modify the code below accordingly).
	print("\n", n, " equations. ", "The solution is:\n", b)
	err = norm(b-soln, ord=inf)
	print("Error (inf-norm of difference)): ", err)

print("^^^(Greater than TOL = ", TOL, ")^^^\n")
print("********************************************\n")
print("Max number of equations while error remains less than ", TOL, " is: ", n-1, "\n") 
print("********************************************")