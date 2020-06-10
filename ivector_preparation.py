#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:45:10 2020

@author: shrutikshirsagar
"""


import pandas as pd
import numpy as np
import scipy.io
import numpy as np
from scipy import stats
from scipy.stats import kurtosis
#descrip = ['X_Centroid', 'X_Crest', 'X_Entropy', 'X_Flatness', 'X_Kurtosis', 'X_Roll', 'X_Skewness', 'X_Slope', 'X_Spread' ]
import matplotlib.pyplot as plt
import scipy.io
import pandas as pd
np_load_old = np.load
from sklearn import preprocessing
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k) # set pickle configuration to True


import pandas as pd
import glob
import numpy as np
path = '/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/train/indoor/' # use your path
all_files = glob.glob(path + "/*.csv")

indoor=np.empty((0, 99))

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0).values
    b = df.T
    
    indoor = np.vstack((indoor, b))
print(indoor.shape)

path = '/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/train/outdoor/' # use your path
all_files = glob.glob(path + "/*.csv")

outdoor=np.empty((0, 99))

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0).values
    b = df.T
   
    outdoor = np.vstack((outdoor, b))
print(outdoor.shape)


path = '/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/train/transportation/' # use your path
all_files = glob.glob(path + "/*.csv")

transportation=np.empty((0, 99))

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0).values
    b = df.T
   
    transportation = np.vstack((transportation, b))
print(transportation.shape)
lbl_indoor = (np.zeros(indoor.shape[0])).astype(int)
lbl_outdoor = (np.ones(outdoor.shape[0])).astype(int)
lbl_transportation = (2*np.ones(transportation.shape[0])).astype(int)

X_train = np.concatenate((indoor, outdoor, transportation))
print(X_train.shape)
y_train = np.concatenate((lbl_indoor, lbl_outdoor, lbl_transportation))
print(y_train.shape)


import pandas as pd
import glob
import numpy as np
path = '/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/test/indoor/' # use your path
all_files = glob.glob(path + "/*.csv")

indoor=np.empty((0, 99))

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0).values
    b = df.T
    
    indoor = np.vstack((indoor, b))
print(indoor.shape)

path = '/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/test/outdoor/' # use your path
all_files = glob.glob(path + "/*.csv")

outdoor=np.empty((0, 99))

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0).values
    b = df.T
   
    outdoor = np.vstack((outdoor, b))
print(outdoor.shape)


path = '/Users/shrutikshirsagar/Downloads/ivector_mfcc_100/test/transportation/' # use your path
all_files = glob.glob(path + "/*.csv")

transportation=np.empty((0, 99))

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0).values
    b = df.T
   
    transportation = np.vstack((transportation, b))
print(transportation.shape)


lbl_indoor = (np.zeros(indoor.shape[0])).astype(int)
lbl_outdoor = (np.ones(outdoor.shape[0])).astype(int)
lbl_transportation = (2*np.ones(transportation.shape[0])).astype(int)

X_test = np.concatenate((indoor, outdoor, transportation))
print(X_test.shape)
y_test = np.concatenate((lbl_indoor, lbl_outdoor, lbl_transportation))
print(y_test.shape)

min_max_scaler = preprocessing.MinMaxScaler()
X_train = min_max_scaler.fit_transform(X_train)
X_test = min_max_scaler.transform(X_test)
np.save('task1b_ivector.npy', np.array([X_train, y_train, X_test, y_test]))