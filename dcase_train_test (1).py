#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:40:26 2020

@author: shrutikshirsagar
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:02:34 2020

@author: shrutikshirsagar
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:40:26 2020

@author: shrutikshirsagar
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:02:34 2020

@author: shrutikshirsagar
"""
import os
import shutil

import fnmatch
import pandas as pd


src_1 = '/media/shrutikshirsagar/Data/Modulation_folder/DCASE/Task1_B_matfiles/Indoor/'
src_2 ='/media/shrutikshirsagar/Data/Modulation_folder/DCASE/Task1_B_matfiles/outdoor/'
src_3 = '/media/shrutikshirsagar/Data/Modulation_folder/DCASE/Task1_B_matfiles/transportation/'
dst_1= "/media/shrutikshirsagar/Data/Modulation_folder/DCASE/Data/test/Indoor/"
dst_2 = "/media/shrutikshirsagar/Data/Modulation_folder/DCASE/Data/test/outdoor/"
dst_3 = "/media/shrutikshirsagar/Data/Modulation_folder/DCASE/Data/test/transportation/"


if not os.path.exists(dst_1): 
    os.makedirs(dst_1)
if not os.path.exists(dst_2): 
    os.makedirs(dst_2)
if not os.path.exists(dst_3): 
    os.makedirs(dst_3)
    #read csv file

    #read csv file
df = pd.read_csv("/media/shrutikshirsagar/Data/Modulation_folder/fold1_test.csv")
print(df.shape)


for index, row in df.iterrows():
    a = row['filename']
    b = a.split("/" )
    
    #myList = [i.split('\t')[0] for i in b] 
    
    ref_file = os.path.splitext(b[1])[0]
    #print(ref_file)
   
    for filename in os.listdir(src_1):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
           shutil.move(os.path.join(src_1, filename), os.path.join(dst_1, filename))
    
    for filename in os.listdir(src_2):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_2, filename), os.path.join(dst_2, filename))
    for filename in os.listdir(src_3):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_3, filename), os.path.join(dst_3, filename))
            
    
    
    

    
    
    
               





