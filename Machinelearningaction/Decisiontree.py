"""
Auther: 
Date: 2018/6/18
"""
# !/usr/bin/python
# -*-coding:utf-8 -*-
from math import log

def calcShannonEnt(dataSet):
	"计算熵"
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		# 如果label不在当前词典中
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannonEnt -= prob * log(prob, 2)
	return shannonEnt

def createDataSet():
	"创建数据集"
	dataSet = [[1, 1, 'yes'],
				[1, 1, 'yes'],
				[1, 0, 'no'],
				[0, 1, 'no'],
				[0, 1, 'no']]
	labels = ['no surfacing', 'flippers']
	return dataSet, labels

def splitDataSet(dataSet, axis, value):
	""
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
return retDataSet
