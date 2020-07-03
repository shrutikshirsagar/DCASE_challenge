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

src_1= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/Airport/"
src_2= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/shopping_mall/"
src_3= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/metro_station/" 
src_4= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/street_pedestrian/"
src_5= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/Public_square/"
src_6= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/street_traffic/"
src_7= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/tram/"
src_8= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/bus/"
src_9= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/metro/"
src_10= "/media/shrutikshirsagar/Data/Modulation_folder/Task_1A_matfiles/park/"

dst_1= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/Airport/"
dst_2= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/shopping_mall/"
dst_3= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/metro_station/" 
dst_4= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/street_pedestrian/"
dst_5= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/Public_square/"
dst_6= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/street_traffic/"
dst_7= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/tram/"
dst_8= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/bus/"
dst_9= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/metro/"
dst_10= "/media/shrutikshirsagar/Data/Modulation_folder/Data/test/park/"

if not os.path.exists(dst_1): 
    os.makedirs(dst_1)
if not os.path.exists(dst_2): 
    os.makedirs(dst_2)
if not os.path.exists(dst_3): 
    os.makedirs(dst_3)
if not os.path.exists(dst_4): 
    os.makedirs(dst_4)
if not os.path.exists(dst_5): 
    os.makedirs(dst_5)
if not os.path.exists(dst_6): 
    os.makedirs(dst_6)
if not os.path.exists(dst_7): 
    os.makedirs(dst_7)
if not os.path.exists(dst_8): 
    os.makedirs(dst_8)
if not os.path.exists(dst_9): 
    os.makedirs(dst_9)
if not os.path.exists(dst_10): 
    os.makedirs(dst_10)
    #read csv file

    #read csv file
df = pd.read_csv("/home/shrutikshirsagar/Downloads/Task1A/fold1_test.csv")
print(df.shape)


for index, row in df.iterrows():
    a = row['filename\tscene_label']
    b = a.split("/" )
    
    myList = [i.split('\t')[0] for i in b] 
    
    ref_file = os.path.splitext(myList[1])[0]
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

    for filename in os.listdir(src_4):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_4, filename), os.path.join(dst_4, filename))
    for filename in os.listdir(src_5):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_5, filename), os.path.join(dst_5, filename))

    for filename in os.listdir(src_6):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_6, filename), os.path.join(dst_6, filename))

    for filename in os.listdir(src_7):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_7, filename), os.path.join(dst_7, filename))
    for filename in os.listdir(src_8):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_8, filename), os.path.join(dst_8, filename))
    for filename in os.listdir(src_9):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_9, filename), os.path.join(dst_9, filename))
    for filename in os.listdir(src_10):
        filenames = os.path.splitext(filename)[0]
        #print(filenames)
        if fnmatch.fnmatch(filenames,  ref_file):
            shutil.move(os.path.join(src_10, filename), os.path.join(dst_10, filename))
 
            
    
    
    

    
    
    
               





