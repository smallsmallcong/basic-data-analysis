import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt

###根据指定的速度值或者速度区间，计算速度对应的污染物浓度平均值、分位数等

vel_path = r"D:\Study\vehicle\data\second-result"
vel_path2 =r"D:\Study\vehicle\speed"
sample_file = r"sample_data.csv"
full_file = r"vel_all.csv"
pass_file = r"pass_ID.csv"
sec_file =r"sec_resl.csv"
outpath = r"D:\Study\vehicle\test_line\0810"
sample = os.path.join(vel_path, sample_file)
pass_vel = os.path.join(vel_path, pass_file)
percentile = [0.01,0.05,0.10,0.25,0.50,0.75,0.90,0.95,0.99]
index_list = ["count","mean","std","min","1%","5%","10%","25%","50%","75%","90%","95%","99%","max"]
# sample_data = pd.read_csv(sample,usecols = [1,2,3,4,5,6,7,8])
# full_data = pd.read_csv(os.path.join(vel_path, full_file),usecols = [1,2,3,4,5,6,7,8,25,26,27,28])

sec_data = pd.read_csv(os.path.join(vel_path, sec_file))
sec_data = sec_data[sec_data.尾气检测合格与否==1]

V = np.array(sec_data["逐秒车速"]).reshape(-1,1)
# NO = np.array(sec_data["逐秒NO浓度"]).reshape(-1,1)
# CO = np.array(sec_data["逐秒CO浓度"]).reshape(-1,1)
HC = np.array(sec_data["逐秒HC浓度"]).reshape(-1,1)

plt.scatter(V,HC, s=8, c="red", alpha=0.5, marker="o")
plt.xlabel('Speed', fontsize=15)
plt.ylabel('HC', fontsize=15)
title = "SEC_V-HC"
plt.title(title, fontsize=20, verticalalignment='bottom')
plt.savefig("SEC_V-HC.png")



# clos = full_data.columns.values
# cols_df = pd.DataFrame(clos)
# # print(full_data.columns.values)
# cols_df.to_csv("full_cols.csv")
## pass_df = pd.read_csv(pass_vel)
# pass_list = pass_df["ID"].tolist()


#
# speed_list = [0,5,10,15,20,25,30,35,40,45,50,55,60]
# col_list = ["逐秒NO浓度","逐秒CO浓度","逐秒HC浓度"]
#
# for speed in speed_list:
#     for col in col_list:
#         df_slice = sec_data[col][sec_data.逐秒车速==speed]
#         emis_stat = df_slice.describe(percentiles=percentile)
#         emis_stat = pd.DataFrame(emis_stat, index=index_list).T
#         speed_tag = str(speed)+" km/h"
#         emis_stat =emis_stat.rename(index = {col:speed_tag})
#         outname = str(col)+"_"+str(speed)+".csv"
#         outfile = os.path.join(vel_path2,outname)
#         emis_stat.to_csv(outfile)