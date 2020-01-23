import pylab as lab
from math import *

x = []
linear = []
quad = []
cubic = []
exp = []

for i in range (30):
    x.append(i)
    linear.append(i)
    quad.append(pow(i, 2))
    cubic.append(pow(i, 3))
    exp.append(pow(1.5, i))

lab.plot(x, linear)
lab.plot(x, quad)
lab.plot(x, cubic)
lab.plot(x, exp)
