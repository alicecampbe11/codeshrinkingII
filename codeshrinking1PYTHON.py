#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:47:22 2022

@author: alicecampbell
"""

import random

agents = []

y0 = random.randint(0,99)
x0 = random.randint(0,99)

agents.append([y0,x0])

print(agents)

print(y0)

print(x0)


if random.randint(0,99) < 50:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
print(y0) 

if random.randint(0,99) < 50:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print(y0, x0)

y1 = 50
x1 = 50

print(y1)
print(x1)

if random.randint(0,99) < 50:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
print(y1) 

if random.randint(0,99) < 50:
    x1 = x1 + 1
else:
    x1 = x1- 1
print(y1, x1)


y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff    
sum2 = y_diffsq + x_diffsq
answer = sum2**0.5

print(answer)

#have shrunk code here to get rid of y0,x0 and clean it up 

import random

agents = []
agents.append([random.randit(0,99),random.randit(0,99)])

print(agents)

# now resetting y1 and x1 to agents list like i have done above.copy and pasting all the code


import random

agents = []

y0 = random.randint(0,99)
x0 = random.randint(0,99)

agents.append([y0,x0])

print(agents)


if random.randint(0,99) < 50:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
print(y0) 

if random.randint(0,99) < 50:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print(y0, x0)

y1 = random.randint(0,99)
x1 = random.randint(0,99)

agents.append([y0,x0],[y1,x1])

print(y1)
print(x1)

print(agents)

if random.randint(0,99) < 50:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
print(y1) 

if random.randint(0,99) < 50:
    x1 = x1 + 1
else:
    x1 = x1- 1
print(y1, x1)

