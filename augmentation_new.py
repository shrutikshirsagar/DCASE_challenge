#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:17:27 2020

@author: shrutikshirsagar
"""


import numpy as np
from numpy.lib.stride_tricks import as_strided
from sklearn import metrics
import scipy.io as sio

import itertools
import os
import sys
import pickle
from time import sleep
import random
from scipy.signal import convolve2d
import argparse
from tempfile import NamedTemporaryFile




def augment_audio(path, outp, sample_rate,tempo, gain):
    
    sox_augment_params = ["tempo", "{:.3f}".format(tempo), "gain", "{:.3f}".format(gain)]
    #sox_param = "sox -t wav \"{}\" -r {} -c 1 -b 16 -e signed {} \"{}\" >/dev/null 2>&1".format(path, sample_rate, outp, " ".join(sox_augment_params)) 
    sox_param = "sox -t wav \"{}\" -r {} -c 1 -b 16 -e signed {} {} ".format(path, sample_rate, outp, " ".join(sox_augment_params))                            
    a = os.system(sox_param)
    print('a', a)
def load_randomly_augmented_audio(path, sample_rate=16000, tempo_range=(0.85, 1.15), gain_range=(-6, 8)):
    """
    Picks tempo and gain uniformly, applies it to the utterance by using sox utility.
    Returns the augmented utterance.
    """
    low_tempo, high_tempo = tempo_range
    tempo_value = np.random.uniform(low=low_tempo, high=high_tempo)
    low_gain, high_gain = gain_range
    gain_value = np.random.uniform(low=low_gain, high=high_gain)
    audio = augment_audio(path=path, outp= outp, sample_rate=sample_rate, tempo=tempo_value, gain=gain_value)
  
    return audio
path = '/Users/shrutikshirsagar/Downloads/audio-data-augmentation-master/data/'
out =  '/Users/shrutikshirsagar/Downloads/audio-data-augmentation-master/new/'
for root,dirs,filenames in os.walk(path):
  
    for file in filenames:
        for i in range(5):
            
            print(file)
             
            a= file.split('.')[0]
            filenew = a+ '_' + str(i)+ '.wav'
            print(filenew)
            outp = os.path.join(out ,filenew)
            print(outp)
            data = load_randomly_augmented_audio(os.path.join(root,file))  
        


