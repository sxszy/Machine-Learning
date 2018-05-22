# import
import numpy as np
from Q1 import fcf
from Q2a import feature

# Create matrix Xtrain and Xtest
Xtrain = np.zeros((40,len(feature)))
Xtest = np.zeros((10,len(feature)))

# Start to store the occurrence
for i in range(0,50):
    f = open(fcf[i],'r',errors = 'ignore')
    text = f.read()
    if i <= 39:
        for j in range(len(feature)):
            Xtrain[i,j] = text.count(feature[j])
    else:
        for j in range(len(feature)):
            Xtest[i-40,j] = text.count(feature[j])
print(Xtrain)

# Acquire the lables of samples
a = np.zeros((20,1))
b = np.ones((20,1))
c = np.append(a,b)
Y = c.reshape(40,1)
print(Y)
