import pandas as pd
import numpy as np
import os,sys,glob
import base

#把结构相同的n个dataframe加在一起（行列索引相同的元素进行求和）
#注意最开始的df不能为空的Dataframe

path = r"D:\Study\筛选"
path2 = r"D:\Study\筛选\O3-RH"
emp = r"emp.csv"

i =0
df = pd.read_csv(os.path.join(path2,emp))
all_files = glob.glob(os.path.join(path, ('*' + '.csv')))

while i < len(all_files):
    temp_df = pd.read_csv(all_files[i])
    df = df+ temp_df
    i =i+1
outname = "test" + ".csv"
df.to_csv(os.path.join(path2, outname), encoding='utf_8_sig', index=None)

