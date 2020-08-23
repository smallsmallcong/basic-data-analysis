import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt


vel_path = r"D:\Study\vehicle\data\second_reslut_order"
sample_file = r"f1000.csv"
sample = os.path.join(vel_path, sample_file)

sample_data = pd.read_csv(sample) ##,usecols = [0,1,2,3,4,5,6,7,8,26,27,28]

cols= sample_data.columns.tolist()
df_clos= pd.DataFrame(cols)
outfile  = r"order_clos.csv"
df_clos.to_csv(os.path.join(vel_path, outfile))

# list2= sample_data["每次检验编号"].tolist()
# list_id = list(set(list2))
# list_id.sort(key=list2.index)
# df2 = pd.DataFrame(list_id)
# out = r"list_ID.csv"
# df2.to_csv(os.path.join(vel_path, out))


# vel_passed = sample_data[(sample_data["尾气检测合格与否"]==1)]
# vel_failed = sample_data[(sample_data["尾气检测合格与否"]==0)]
# list1 = vel_passed["每次检验编号"].tolist()
# list0 = vel_failed["每次检验编号"].tolist()
#
# pass_list = list(set(list1))
# pass_list.sort(key=list1.index)
#
# fail_list = list(set(list0))
# fail_list.sort(key=list0.index)
#
# df1 = pd.DataFrame(pass_list)
# df1.to_csv("pass_ID.csv")
#
# df0 = pd.DataFrame(fail_list)
# df0.to_csv("fail_ID.csv")