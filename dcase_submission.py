#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:09:08 2020

@author: shrutikshirsagar
"""


##final submission
import sklearn
from sklearn import preprocessing
from sklearn import decomposition
from sklearn import datasets
import glob
import os
import pandas as pd
import numpy as np
import joblib
from sklearn import svm
output_fin1=np.empty((0,5))

output_cols=['filename', 'scene_label', 'indoor', 'outdoor', 'transportation']
##to read test csv files
path = '/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/try_test/' # use your path
all_files = glob.glob(path + "/*.csv")

try_test=np.empty((0, 5))
scene = []
for filename in all_files:
    
    df = pd.read_csv(filename, index_col=None, header=None).values
    b = df.T
   
    basename = os.path.basename(filename)
    n = os.path.splitext(basename)[0]
    filename = n +'.wav'  ##as we have csv features files
    filename = np.array([filename]) 
    filename = filename[:,None]
    filename1 = '/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/finalized_model.sav' ##saved sklearn svm model path
    loaded_model = joblib.load(filename1) ## calling sklearn save model
    
    joblib.dump(clf, filename1) 
    result = clf.predict_proba(b)  ##save your model and then load it here for prob prediction
    result = list(np.around(np.array(result),2))
    result = np.asarray(result, dtype=np.float32)
    out = clf.predict(b)
   
    ##to get scene label
    if out == 0:
        scene = 'indoor'
    elif out == 1:
        scene = 'outdoor'
    else:
        scene = 'transportation'
    s = np.array([scene])
    s = s[:,None]
    
    b1 = np.hstack((filename, s, result))
    
    try_test = np.vstack((try_test, b1))
    

print(try_test.shape)
df=pd.DataFrame(try_test, columns=output_cols)

df.to_csv('/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/' + 'Test_TAU_task1b_1.output.csv',index=None) ##for task 1b