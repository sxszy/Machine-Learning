# !/usr/bin/python
# -*-coding:utf-8 -*-
# import sys
# sys.path..append("...")
# import file

"""
Auther: 
Date: 2018/6/12
"""

from numpy import *  
import operator  
   
def createDataSet():  
	"""
	创建一个数据集
	"""
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])  
	labels = ['A','A','B','B']  
	return group,labels

def classify0(inX,dataSet,labels,k):  
	"""
	分类
	"""
	dataSetSize = dataSet.shape[0]	
	# tile, 是把inX在行上重复dataSetSize，列上重复1次
	# 计算每个点与目标点的差
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	# 取平方
	sqDiffMat = diffMat**2
	# 将各个维度平方相加 
	sqDistances = sqDiffMat.sum(axis = 1)
	# 开平方
	distances = sqDistances**0.5	
	# 排序
	sortedDistIndicies = distances.argsort()	
	classCount = {}	
	for i in range(k):	
		# 取标签
		voteIlabel = labels[sortedDistIndicies[i]]	
		# 对该类加一
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),
								key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]	

def file2matrix(filname):
	"""
	将文件转成numpy
	"""
	# 打开文件
	fr = open(filname)
	# 用于读取所有行，如果是readline（），读取第一行
	arrayOLines = fr.readlines()
	numberOFLines = len(arrayOLines)
	returnMat = zeros((numberOFLines, 3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		# 去除首尾空格
		line = line.strip()
		# 以"\t"为分隔符进行分割
		listFromLine = line.split('\t')
		# 把特征值赋值给returnMat
		returnMat[index,:] = listFromLine[0:3]
		# 把标签给对应向量
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat, classLabelVector

def autoNorm(dataSet):
	# 分别存放每一列的最大最小值
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	# 取值范围就可以通过他们的差来得出
	ranges = maxVals - minVals
	# 创建一个与原来相同的大小
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	# 扣去最小值再除以范围就可以normalize
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet, ranges, minVals
