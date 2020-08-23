import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt

vel_path = r"D:\Study\vehicle\data"
sample_file = r"sample_data.csv"
sample = os.path.join(vel_path, sample_file)

sample_data = pd.read_csv(sample,usecols = [1,2,3,4,5,6,7,8])

slice_vsp = sample_data["vsp"]
x = slice_vsp.tolist()

fig, ax = plt.subplots(figsize=[20,10])
bins = range(-40,100,5)
plt.hist(x, bins, density=True,label="VSP bin", rwidth=0.85)

ax.legend(loc='upper center',bbox_to_anchor=(0.6,0.95))
font1 = {'family': 'Times New Roman','weight': 'normal','size': 20,}  #图例的字体设置,prop参数适用于plt.legend
plt.legend(prop=font1)

x_tic = bins
ax.xaxis.set_ticks(x_tic)

ax.set_xticklabels(x_tic,size=20)

ax.tick_params(direction='in',width=2,length=6)
# y_tic = np.linspace(0,0.10,5)
y_tic = [0,0.02,0.04,0.06,0.08,0.10]
ax.yaxis.set_ticks(y_tic)
ax.set_yticklabels(y_tic,size = 20)

plt.xlabel('VSP bin',fontsize=22)
plt.ylabel('frequency',fontsize=22)
title = "VSP bin"
plt.title(title,fontsize=25,verticalalignment='bottom')

ax=plt.gca()#获得坐标轴的句柄
width_x = 2.5
ax.spines['bottom'].set_linewidth(width_x)###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(width_x)####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(width_x)###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(width_x)###设置上边坐标轴的粗细

out_name = "vsp_bin5"+'.png'

outpath = r"D:\Study\vehicle\test_bin"
outfile = os.path.join(outpath,out_name)
plt.savefig(outfile)
# plt.show()
# print(slice_df)
# ave = sample_data.mean()
