import numpy as np
import random


    ##def __init__(self):
    # Random linearly separated data
V = []
X = []
N = 1000
## This gives about 1000 points
for i in range(1000):
    xA,yA,xB,yB = [random.uniform(-1, 1) for i in range(4)]
    v = np.array([xB*yA-xA*yB, yB-yA, xA-xB])
    x1,x2 = [random.uniform(-1, 1) for i in range(2)]
    x = np.array([1,x1,x2])
    s= int(v.transpose().dot(x))
    X .append((x,s))
print(X)

## Plot these points to see how exactly they look 
