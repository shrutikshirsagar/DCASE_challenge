#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:06:53 2020

@author: shrutikshirsagar
"""
import matplotlib.pyplot as plt
import scipy.io

descrip = ['X_Centroid', 'X_Crest', 'X_Entropy', 'X_Flatness', 'X_Kurtosis', 'X_Roll', 'X_Skewness', 'X_Slope', 'X_Spread' ]
T = scipy.io.loadmat('/Users/shrutikshirsagar/Downloads/DCASE/T.mat')
M = T['T']
print(M.shape)
for i in descrip:
    print(i)
    mat = scipy.io.loadmat('/Users/shrutikshirsagar/Downloads/DCASE/Test/test_indoor.mat')
    a = mat[i]
    print(a.shape)
    b = a.mean(0)
    print(b.shape)
    
    mat = scipy.io.loadmat('/Users/shrutikshirsagar/Downloads/DCASE/Test/test_outdoor.mat')
    a1 = mat[i]
    print(a1.shape)
    b1 = a1.mean(0)
    print(b1.shape)
    
    
    mat = scipy.io.loadmat('/Users/shrutikshirsagar/Downloads/DCASE/Test/test_transportation.mat')
    a2 = mat[i]
    print(a2.shape)
    b2 = a2.mean(0)
    print(b2.shape)
    
    
    
    plt.plot(b, label = "Indoor")
    plt.plot(b1, label = "outdoor")
    plt.plot(b2, label = "transporttaion")
    plt.title(i) 
    print(b.shape)
    print(b1.shape)
    print(b2.shape)
    plt.legend()

    plt.savefig('/Users/shrutikshirsagar/Downloads/DCASE/Test/'+i+'.png')
    plt.clf()