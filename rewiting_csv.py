import glob
import os
import numpy as np
import pandas as pd

sets = {'train', 'test' };
classes = {'Indoor', 'outdoor', 'transportation'};
for c in classes:
    for s in sets:
        feature_folder_train = "/media/shruti/Data/Modulation_folder/Data_MSF_223_sd/" + s + "/" + c + "/"
        output = "/media/shruti/Data/Modulation_folder/MSF_SD/"+ s + "/" + c + "/"
        if not os.path.exists(output):
            os.makedirs(output) 
        for filename in os.listdir(feature_folder_train):
            filename1= os.path.join(feature_folder_train,filename)
            print(filename1)
            df = pd.read_csv(filename1, index_col=None, header=None).values
          
            df = df[:, 184:223]
          
            df=pd.DataFrame(df)
            df.to_csv(output+filename.split('/')[-1].split('.')[0]+'.csv', index = False, header=None)

