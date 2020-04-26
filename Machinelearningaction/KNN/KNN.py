# !/usr/bin/python
# -*-coding:utf-8 -*-
# import sys
# sys.path..append("...")
# import file
"""
Auther: Peter Harrington 
Note：Szy
Date: 2018/6/12
"""

from numpy import *  
import os
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
	sortedClassCount = sorted(classCount.items(),
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
	"""
	规划化数据集
	"""
	# 分别存放每一列的最大最小值
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	# 取值范围就可以通过他们的差来得出
	ranges = maxVals - minVals
	# 创建一个与原来相同的大小
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	# 扣去最小值再除以范围就可以normalize
	normDataSet = dataSet - tile(minVals, (m,1))
	normDataSet = normDataSet/tile(ranges, (m,1))
	return normDataSet, ranges, minVals


def datingClassTest():
	"""
	进行测试
	"""
	hoRatio = 0.10
	# 调用函数进行格式转换
	datingDataMat, datingLabels = file2matrix('datingSet2.txt')
	# Normalize
	normMat, ranges, minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	# 取1/10作为测试集
	numTestVecs = int(m * hoRatio)
	# 初始化错误率
	errorCount = 0.0
	for i in range(numTestVecs):
		# 分类
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],\
			datingLabels[numTestVecs:m],3)
		print("the classifier came back with: %d, the real answer is: %d"\
			%(classifierResult, datingLabels[i]))
		if (classifierResult != datingLabels[i]): errorCount += 1.0
	print("the total error rate is :%f" %(errorCount/float(numTestVecs)))

def classifyPerson():
	"""
	对于一个新输入的判别
	"""
	# resultList里存放的是三类结果的标签
	resultList = ['not at all','in small doses','in large doses']
	# 输入三个特征
	percentTats = float(input(\
				"percentage of time spent playing video games? "))
	ffMiles = float(input("frequent flier miles earned per year? "))
	iceCream = float(input("liters of ice cream consumed per year? "))
	datingDataMat,datingLabels = file2matrix('datingSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr-\
		minVals)/ranges,normMat,datingLabels,3)
	print("You will probably like this person:",\
		resultList[classifierResult - 1])

def img2vector(filename):
	"""
	转成普通的int
	"""
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		LineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(LineStr[j])
	return returnVect

def handwritingClassTest():
	"""
	对手写数字数据集进行训练和测试
	"""
	# 读取训练集及标签
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    # 读取测试集并测试
    testFileList = os.listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    # 显示错误率
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total error rate is: %f" % (errorCount/float(mTest)))
