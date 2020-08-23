import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt

vel_path = r"D:\Study\vehicle\data"
detail_file = r"vel.csv"
ins_file = r"result_full.csv"
rename_file = r"rename.csv"
detail_data = pd.read_csv(os.path.join(vel_path, detail_file))
ins_data = pd.read_csv(os.path.join(vel_path, ins_file))
name = pd.read_csv(os.path.join(vel_path, rename_file),header = None,encoding="gbk") #存在中文，编码为gbk,若保存时存为utf-8则无须声明编码
a = name.iloc[:,0]
b = name.iloc[:,1]
c = dict(zip(a,b))
ins_data.rename(columns=c,inplace = True)

vel_detail= pd.merge(ins_data,detail_data,on = "车辆型号", how = 'outer')

# detail_data = detail_data.set_index("车辆型号")
# print(detail_data.head())

# inspec_data = inspec_data.set_index("每次检验编号")
# inspec_data = inspec_data.rename(colunms = {"SXKSSJ":"车辆检测时间","PDJD":"车辆排放标准","车辆注册型号":"车辆型号"})
vel_detail= vel_detail.set_index("每次检验编号")
# clos = vel_detail.columns.values
# col_df = pd.DataFrame(clos)
vel_detail = vel_detail.iloc[:,:68]
out_name = "vel_detail.csv"
outfile = os.path.join(vel_path,out_name)
vel_detail.to_csv(outfile)

# col_df.to_csv("vel_detail_cols.csv")
# print()
# print(name)