"""
Auther: szy
Date: 2018/4.23
"""

import os
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.feature_extraction.text import CountVectorizer
import glob
import numpy as np
from sklearn . naive_bayes import MultinomialNB
from sklearn .model_selection import KFold

# ======================== Aquire the input ===============================
# auto - 1, baseball - 2, electronics
fcf = glob.glob('F:\HKU\data mining\dataset-news\*')
fcf = sorted(fcf)
list = []
list1 = []
for i in range(len(fcf)):
    text = open(fcf[i], 'r')
    raw_message = text.read()
    raw_message = raw_message.rstrip('\n')
    message = [raw_message]
    list = list + message
#     if 'mac-hw' in fcf[i]:
#         list1 = list1 + message
#     elif 'hockey' in fcf[i]:
#         list1 = list1 + message
#     elif 'pol-guns' in fcf[i]:
#         list1 = list1 +message
# print(list1)

# ======================== Run the CountVectorizer =========================
count_vect = CountVectorizer(stop_words=['a','the','my','yours','an','her','his'])
X_train_counts = count_vect.fit_transform(list)
X = X_train_counts.toarray()
y = []
y1 = []
for i in range(8):
    tmp = (i + 1) * np.ones(100 * 1)
    y = np.append(y, tmp)
print(y)
# for j in range(3):
#     tmp1 = (j + 1) * np.ones(100 * 1)
#     y1 = np.append(y1, tmp1)for j in range(3):
#     tmp1 = (j + 1) * np.ones(100 * 1)
#     y1 = np.append(y1, tmp1)

# ========================Peform Bayes Gaussian ======================
kf = KFold(n_splits = 10, shuffle = True)
acc = []
acc1 = []
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred1 = gnb.predict(X_test)
    new = np.random.randint(1, 9, 80)
    acc = np.append(acc, (y_test == y_pred1).sum()/X_test.shape[0])
    acc1 = np.append(acc1, (y_test == new).sum() / X_test.shape[0])
# print("gaussian average accuracy", np.mean(acc))
print(np.mean(acc1))

# ========================Peform Bayes multinomial ===================
kf = KFold(n_splits = 10, shuffle = True)
acc = []
acc1 = []
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    mnb = MultinomialNB(alpha=1.0)
    mnb.fit(X_train, y_train)
    y_pred2 = mnb.predict(X_test)
    new = np.random.randint(1, 9, 80)
    acc = np.append(acc,(y_test == y_pred2).sum()/X_test.shape[0])
    acc1 = np.append(acc1, (y_test == new).sum() / X_test.shape[0])
# print("multinomial average accuracy", np.mean(acc))
print(np.mean(acc1))





