import pandas as pd
import numpy as np
import os

path = r"D:\Study\萧山机动车\年检数据"
file1 = r"rename2.csv"
file2 = r"result_full.csv"
namefile = os.path.join(path, file1)
datafile = os.path.join(path, file2)

#该文件(rename2.csv)为空格分隔，所以加了一句delim_whitespace = True,不包含表头，所以,header=None
name = pd.read_csv(namefile,delim_whitespace=True,header = None)

vel_data = pd.read_csv(datafile)
a = name.iloc[:,0]
b = name.iloc[:,1]
c = dict(zip(a,b))
vel_data.rename(columns=c,inplace = True)
vel_data.to_csv('vel_data.csv',encoding='utf-8')
#print(c)