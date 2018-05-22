#  import
import numpy as np
import matplotlib.pyplot as plt
from Q2b import Xtrain, Xtest

#  Compute the XTX, Xtrain(40 x 13)
meanX = np.mean(Xtrain,axis = 0)
Ctrx = Xtrain - meanX
XTX = np.dot(Ctrx.T, Ctrx)
Cxx=1.0/(Xtrain.shape[0]-1)*XTX
print("Cxx = ", Cxx)

#  V-principal components
D,V = np.linalg.eig(Cxx)
print("D = ",D)
print("V = ",V)

#  PC(13 x 2)
PC = V[:,0:2]
print("PC = ", PC)

#  Obtain the PC score
t = np.dot(Xtrain,PC)
print("t = ",t)

# Plot
fig = plt.figure(figsize=(8,5))
plt.scatter(t[0:19:,0],t[0:19:,1],s=30,c='red',marker='o',alpha=0.5,label='class0')
plt.scatter(t[20:39:,0],t[20:39:,1],s=30,c='g',marker='o',alpha=0.5,label='class1')
axes = plt.gca()
axes.set_xlim([-8,5])
axes.set_ylim([-2,8])
plt.legend(loc='upper right')
plt.title('PC Scores ')
plt.xlabel('PCA 1')
plt.ylabel('PCA2')
plt.show()

