"""
Auther: szy
Date: 2018/4.23
"""

from sklearn.datasets import load_iris
import pandas as pd
from sklearn import tree
import os
os.environ["PATH"] += os.pathsep + 'D:/Graphviz/bin/'

# =======================Input======================================
df = pd.read_csv('Skyserver.csv', parse_dates=[1])
X = df[['ra','dec','u','g','r','i','z','run','rerun','camcol','field','specobjid','redshift',\
        'plate','mjd','fiberid']]
y = pd.read_csv('training_class.csv')
featurename = ['ra','dec','u','g','r','i','z','run','rerun','camcol','field','specobjid','redshift',\
        'plate','mjd','fiberid']

# =========================== Train the decision tree ======================
clf = tree.DecisionTreeClassifier(min_samples_leaf=100,min_impurity_split = 1e-1)
clf = clf.fit(X, y)
import graphviz # doctest: +SKIP
dot_data = tree.export_graphviz(clf, out_file=None) # doctest: +SKIP
# graph = graphviz.Source(dot_data) # doctest: +SKIP
# # graph.render("decision2") # doctest: +SKIP
# dot_data= tree.export_graphviz(clf, out_file=None,
#                                 feature_names=['ra','dec','u','g','r','i','z','run','rerun','camcol','field','specobjid','redshift',\
#         'plate','mjd','fiberid'],
#
#                                 class_names='class')  # doctest: +SKIP
#                                 # filled=True, rounded=True,  # doctest: +SKIP
#                                 # special_characters=True)  # doctest: +SKIP)
# graph = graphviz.Source(dot_data)  # doctest: +SKIP
# graph # doctest: +SKIP
l = clf.tree_.children_left
l1 = clf.tree_.children_right
print(l)
# print(clf.tree_.value[7])
# print(clf.tree_.value[8])
# print(clf.tree_.value[9])
# =========================== Define generation error ======================
def error(model, l, inputX, inputy):
    "Compute the generation error"
    trainingerror = 1 - model.score(inputX,inputy)
    print(trainingerror)
    number = len([i for i, v in enumerate(l) if v == -1]) # Number of leafs
    generationerror = trainingerror + (0.5 * number)/10000 # Generation error
    return generationerror

# =========================== Acquire the generation error =================

generationerror = error(clf,l, X, y)
print(generationerror)

# =========================== Post prune ===================================
trainpuned = (23 + 1 + 4 + 849)
generpruned = (trainpuned + 0.5 * 2) / 10000

if generationerror > generpruned:
    print("pruned")
else:
    print("No change")
