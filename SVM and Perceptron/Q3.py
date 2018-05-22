#  import
import numpy as np
import matplotlib.pyplot as plt
from cvxopt import solvers
from cvxopt import matrix
from Q3 import t

# The funtion of Y matrix
def create(t):
    X1 = t[0:20, :]
    X2 = t[20:40, :]
    Y1=np.concatenate((np.ones((20,1)), X1), axis=1)
    Y2=np.concatenate((np.ones((20,1)) * -1, -X2), axis=1)
    Y=np.concatenate((Y1, Y2), axis=0)
    return Y

# Y matrix of dimension 3
Y = create(t)

# The function of Perceptron
def perceptron(Y,dimension):
    # Initialize
    a = np.zeros((dimension, 1))
    a_iter = a
    k = 0
    # Number of misclassified samples
    sum_wrong = 1
    while sum_wrong > 0 and k < 1000:
        wrong = np.dot(Y, a_iter) <= 0 # Wrong is matrix of  40 * 1,every element is true or false.
        sum_wrong = sum(wrong) # Count the number of error
        sum1 = sum(wrong * np.ones((1,dimension)) * Y) # Caculate the sum of yi
        a_iter = a_iter + sum1.reshape(dimension,1) # To improve the a_iter
        k = k + 1
    a_con = a_iter
    return a_con

# Acquire a paramater
a_con = perceptron(Y,3)
x = np.arange(-1,10,5)
y = -(a_con[0] + a_con[1] * x) /a_con[2]

# Plot
def plotf(x, y, t, title):
    fig1 = plt.figure(figsize=(8,8))
    plt.scatter(t[0:19:,0],t[0:19:, 1],s=10, c='r', marker='o', alpha=0.5, label='class0')
    plt.scatter(t[20:39:,0],t[20:39:, 1],s=10, c='g', marker='o', alpha=0.5, label='class1')
    plt.legend('upper right')
    plt.title(title)
    plt.xlabel('PCA 1')
    plt.ylabel('PCA 2')
    axes = plt.gca()
    axes.set_xlim([-8,5])
    axes.set_ylim([-4,6])
    plt.plot(x, y)
    plt.show()

# Plot Perceptron
plotf(x,y,t,'Perceptron Plot')

# SVM part
def SVM(Y,dimension):
    A = matrix(Y,tc='d')
    b = matrix(-1*np.ones((40,1)),tc='d')
    q1 = np.zeros((1, dimension))
    Q2 = np.concatenate((np.zeros((dimension - 1,1)), np.eye(dimension - 1)),axis=1) # np.eye()可以生成对角矩阵
    Q = np.concatenate((q1,Q2),axis=0)
    Q = matrix(2*Q,tc='d')
    q = matrix(np.zeros((dimension,1)),tc='d')
    sol = solvers.qp(Q,q,A,b)
    a_con = sol['x']
    return a_con

# Acquire the parameters
a_con = SVM(Y, 3)
x = np.arange(-1,10,5)
y = -(a_con[0]+a_con[1]*x)/a_con[2]

# plot SVM
plotf(x,y,t,'Support vector machine Plot')
