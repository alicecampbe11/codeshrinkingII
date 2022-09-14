#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:55:33 2022

@author: alicecampbell
"""
import operator
import random
import matplotlib.pyplot

random.seed(1)
agents = []

y0 = random.randint(0,99)
x0 = random.randint(0,99)

agents.append([y0,x0])

# 'apend' has given values of y0 and x0 to the agents (sheep). 

print(agents)

y1 = random.randint(0,99)
x1 = random.randint(0,99)

agents.append([y1,x1])

print(y1)
print(x1)

print(agents)

# ([85,48],[37,18]) appears with print agents. is presented as a list but actually a matrix table. 

print(max(agents))

# the above command will find out the coordinate furthest to the east. depends on y1, only look at x0,x1 if the y's are identical

print(max(agents, key=operator.itemgetter(1)))

# the above gives us the max in x direction

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], c = 'MAGENTA')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()

#the above plots agent locations onto the graph. 



