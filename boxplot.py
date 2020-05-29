#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:05:08 2020

@author: shrutikshirsagar
"""


###boxplot
import matplotlib.pyplot as plt
import scipy.io

descrip = ['X_Centroid', 'X_Crest', 'X_Entropy', 'X_Flatness', 'X_Kurtosis', 'X_Roll', 'X_Skewness', 'X_Slope', 'X_Spread' ]


for i in descrip:
    print(i)
    c = []
    mat = scipy.io.loadmat('/Users/shrutikshirsagar/Downloads/DCASE/Test/test_indoor.mat')
    a = mat[i]
    print(a.shape)
    c.append(a)
    b = a.mean(0)
    print(b.shape)
    
    mat = scipy.io.loadmat('/Users/shrutikshirsagar/Downloads/DCASE/Test/test_outdoor.mat')
    a1 = mat[i]
    print(a1.shape)
    c.append(a1)
    b1 = a1.mean(0)
    print(b1.shape)
    
    
    mat = scipy.io.loadmat('/Users/shrutikshirsagar/Downloads/DCASE/Test/test_transportation.mat')
    a2 = mat[i]
    print(a2.shape)
    c.append(a2)
    b2 = a2.mean(0)
    print(b2.shape)
    
    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))
    
    # Create an axes instance
    ax = fig.add_subplot(111)
    
    # Create the boxplot
    bp = ax.boxplot(c)
    ax.set_xticklabels(['Indoor', 'outdoor', 'transportation'])
    ax.set_title(i)
    # Save the figure
    fig.savefig('/Users/shrutikshirsagar/Downloads/DCASE/Test/boxplot/'+i, bbox_inches='tight')
    
    