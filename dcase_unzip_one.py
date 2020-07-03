#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:27:09 2020

@author: shrutikshirsagar
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:23:06 2020

@author: shruti.kshirsagar
"""
##unzip all files in folders
import zipfile,fnmatch,os
import os
import shutil
rootPath = r"D:\databases\DCASE_Challenge\Task_1B\Dataset"
root1 = "D:\databases\DCASE_Challenge\Task_1B\Dataset\data"
pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
        zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root1, os.path.splitext(filename)[0]))
        
##move all unzip files to one file        
rootPath = r"D:\databases\DCASE_Challenge\Task_1B\Dataset\data"
dst = r"D:\databases\DCASE_Challenge\Task_1B\Dataset\data\data_prepared"

for root, dirs, files in os.walk(rootPath):
    for filename in files:
        print(os.path.join(root, filename))
      
        shutil.move(os.path.join(root, filename), os.path.join(dst, filename))