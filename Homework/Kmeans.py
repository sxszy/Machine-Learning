"""
Auther: szy
Date: 2018/4.23
"""

#import
from sklearn.cluster import KMeans
import numpy as np
import csv
import Orange

## Read the file
data = Orange.data.Table("stock_data.csv")
data1 = np.array(data)

## Normalization
for j in range(30):
    data1[j] = data1[j] / np.linalg.norm(data1[j],ord=2)
print(data1)

## Run the Kmeans
estimator = KMeans(n_clusters = 8, n_init=40000)
estimator.fit(data1)# Cluster
label_pred = estimator.labels_ # Acquire the label
centroids = estimator.cluster_centers_ # Acquire the center
inertia = estimator.inertia_ # SSE
print(inertia)
print(label_pred)

## Find the cluster
for k in range(8):
    l = []
    for i in range(30):
        if label_pred[i] == k:
            l.append(data[i][-1])
    print("class ",k + 1)
    print(l)

