# 依次打开文件，对特征词进行计数并存储
import numpy as np
from Q1 import fcf
f = open('01.txt','r')
text1 = f.read()
print(text1)
f = open('feature.txt','r')
featuretest = f.read()
feature = featuretest.split() ## Turn String into list, if you use list(), it will be different because the elements would be listed one by one.
feature1 = feature[0]
print(feature1)
occurrence = text1.count(feature1)
print(occurrence)
