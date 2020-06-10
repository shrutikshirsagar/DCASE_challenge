#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:39:58 2020

@author: shrutikshirsagar
"""


import numpy as np

from sklearn import decomposition
from sklearn import datasets
X_train,y_train,X_test,y_test = np.load('task1b_ivector.npy')
print(X_train.shape)
print(X_test.shape)

# pca = decomposition.PCA(n_components=99)
# pca.fit(X_train)
# X_train = pca.transform(X_train)
# X_test =  pca.transform(X_test)

from sklearn import svm

clf = svm.SVC(C=10, break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma=1, kernel='rbf', max_iter=-1,
    probability=False, random_state=None, shrinking=True, tol=0.001,
    verbose=False)

clf.fit(X_train, y_train)  

y_pred=clf.predict(X_test)

acc=100*sum((y_pred-y_test)==0)/len(y_test)

print(acc)

from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

class_names = ['indoor', 'outdoor', 'transportation']
cm = confusion_matrix(y_test,y_pred)

cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
plt.imshow(cm_normalized, interpolation='nearest')
plt.title("confusion matrix")
plt.colorbar(shrink=1)
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names, rotation=45)
plt.yticks(tick_marks, class_names)
print(cm)

#Get the confusion matrix
cm = confusion_matrix(y_test, y_pred)
#array([[1, 0, 0],
#   [1, 0, 0],
#   [0, 1, 2]])

#Now the normalize the diagonal entries
cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
#array([[1.        , 0.        , 0.        ],
#      [1.        , 0.        , 0.        ],
#      [0.        , 0.33333333, 0.66666667]])

#The diagonal entries are the accuracies of each class
cm.diagonal()