#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:02:34 2020

@author: shrutikshirsagar
"""
import os
import shutil

def main():
    src = "/Users/shrutikshirsagar/Downloads/DCASE/"
    dst_1= "/Users/shrutikshirsagar/Downloads/DCASE/Indoor_a"
    dst_2 = "/Users/shrutikshirsagar/Downloads/DCASE/outdoor_a"
    dst_3 = "/Users/shrutikshirsagar/Downloads/DCASE/transportation_a"
    
    if not os.path.exists(dst_1): 
        os.makedirs(dst_1)
    if not os.path.exists(dst_2): 
        os.makedirs(dst_2)
    if not os.path.exists(dst_3): 
        os.makedirs(dst_3)
    for root, dirnames, filenames in os.walk(src):
        for f in filenames:
           if f.startswith(('airport', 'shopping_mall', 'metro_station')):
                shutil.move(os.path.join(root, f), os.path.join(dst_1, f))
           elif f.startswith(('street_padestrian', 'park', 'public_square', 'street_traffic')):
               shutil.move(os.path.join(root, f), os.path.join(dst_2, f))
           elif f.startswith(('bus', 'metro', 'tram')):
               shutil.move(os.path.join(root, f), os.path.join(dst_3, f))
               
               
               

if __name__ == '__main__':
    main()



import os
import shutil


