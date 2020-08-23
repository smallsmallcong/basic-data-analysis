import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt

vel_path = r"D:\Study\vehicle\data"
inspec_file = r"vel_data.csv"
inspec_data = os.path.join(vel_path, inspec_file)
sample_data = pd.read_csv(inspec_data)
sample_data =sample_data.drop(["Unnamed: 0"],axis=1)
sample_data = sample_data.set_index("每次检验编号")

slice_df = sample_data['发动机排量']

x = slice_df.tolist()

fig, ax = plt.subplots(figsize=[20,10])
bins = range(0,5000,20)
# bins = [0,25000,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000]
plt.hist(x, bins, density=True,label="engine", rwidth=0.85)

ax.legend(loc='upper center',bbox_to_anchor=(0.6,0.95))
font1 = {'family': 'Times New Roman','weight': 'normal','size': 20,}  #图例的字体设置,prop参数适用于plt.legend
plt.legend(prop=font1)

# x_tic = bins
# ax.xaxis.set_ticks(x_tic)

# ax.set_xticklabels(x_tic,size=20)

ax.tick_params(direction='in',width=2,length=6)
# # # y_tic = np.linspace(0,0.10,5)
# y_tic = [0,0.05,0.10,0.15,0.20,0.25]
# ax.yaxis.set_ticks(y_tic)
# ax.set_yticklabels(y_tic,size = 20)

plt.xlabel('engine',fontsize=22)
plt.ylabel('frequency',fontsize=22)
title = "engine"
plt.title(title,fontsize=25,verticalalignment='bottom')

ax=plt.gca()#获得坐标轴的句柄
width_x = 2.5
ax.spines['bottom'].set_linewidth(width_x)###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(width_x)####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(width_x)###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(width_x)###设置上边坐标轴的粗细

out_name = "engine_bin"+'.png'

outpath = r"D:\Study\vehicle\test_bin"
outfile = os.path.join(outpath,out_name)
plt.savefig(outfile)


##简单的描述统计
# stat = sample_data.describe()
# stat.to_csv("describe.csv")

# print(sample_data.columns.values)
# print(sample_data.head(10))