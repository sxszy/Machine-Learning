# import
import numpy as np
from Q3 import Xtrain, Xtest, PC, t
from Q4 import create, perceptron, SVM

# Set the true result
Truth = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1]

# Obtain the PC score
test = np.dot(Xtest, PC)

# The funtion of Y matrix
Y = create(t) # Y matrix of dimension 3
Y14 = create(Xtrain) # Y matrix of dimension 14

# Acquire a paramater
a_con = perceptron(Y,3) # a parameter of dimension 3
a_con14 = perceptron(Y14, 14)# a parameter of dimension 14

# Judge the Perceptron
def judgeper(a_con, test, dimension):
    a = (a_con[1:dimension,:]).reshape(1,dimension - 1)
    gt = np.dot(a, test.T)
    gt = gt + (a_con[0] * np.ones((1,10)))
    error1 = gt < 0
    sum_error1 = sum(error1)
    return sum_error1
result1 = judgeper(a_con, test, 3)
result2 = judgeper(a_con14, Xtest, 14)
print("result1 = ", result1)
print("result2 = ", result2)

# x & y of Perceptron
x = np.arange(-1,10,5)
y = -(a_con[0] + a_con[1] * x) /a_con[2]

# Acquire the parameters
a_con = SVM(Y, 3)
a_con14 = SVM(Y14, 14)
x = np.arange(-1,10,5)
y = -(a_con[0]+a_con[1]*x)/a_con[2]

# Caculate SVM
def judgeSVM(a_con, test, dimension):
    new = np.concatenate((np.ones((10,1)), test),axis = 1)
    J = np.dot(a_con.T, new.T)
    error2 = J > 0
    sum_error2 = sum(error2)
    return sum_error2
result3 = judgeSVM(a_con, test, 3)
result4 = judgeSVM(a_con14, Xtest, 14)
print(result3)
print(result4)
error1 = sum((result1 ^ Truth))
error2 = sum((result2 ^ Truth))
error3 = sum((result3 ^ Truth))
error4 = sum((result4 ^ Truth))

# print
print("testing error for PC score, dimension 3 = %", ((error1 / 10) * 100))
print("testing error for PC score, dimension 14 = %",((error2 / 10) * 100))
print("testing error for Xtest, dimension 3 = %",((error3 / 10) * 100))
print("testing error for Xtest, dimension 14 = %",((error4 / 10) * 100))
