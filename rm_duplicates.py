import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt


vel_path = r"D:\Study\vehicle\data"
sample_file = r"sample_data.csv"
sample = os.path.join(vel_path, sample_file)

sample_data = pd.read_csv(sample,usecols = [1,2,3,4,5,6,7,8])
list0 = sample_data["每次检验编号"].tolist()
inspec_list = list(set(list0))
inspec_list.sort(key=list0.index)
df = pd.DataFrame(inspec_list)
df.to_csv("ID.csv")
# print(inspec_list)
# print((len(list0)))

# ###筛选检测合格的进行分析
# vel_detail=vel_detail[vel_detail.尾气检测合格与否==1]
# ###去除排放标准为空白的行
# # print(len(vel_detail))
# vel_detail= vel_detail.dropna(axis = 0,subset = ['排放标准'])