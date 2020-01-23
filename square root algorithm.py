# Kryzstof Kudlak
# 7/7/18
# Algorithm for Square Roots (idea from 6.00.1x MITx


x = 1343454 # number to square root

g = 3 # initial guess
a = 25 # accuracy (number of times the loop runs)

from math import *

for i in range(a):
    print("Root: " + str(g) + " Square: " + str(pow(g,2)))
    g = ((x/g) + g)/2
    
    
