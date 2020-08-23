import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt
##根据指定的检验编号，绘制195秒的折线图

vel_path = r"D:\Study\vehicle\data"
sample_file = r"sample_data.csv"
sample = os.path.join(vel_path, sample_file)

sample_data = pd.read_csv(sample,usecols = [1,2,3,4,5,6,7,8])
# list0 = sample_data["每次检验编号"].tolist()
# inspec_list = list(set(list0))
# inspec_list.sort(key=list0.index)
# print(inspec_list)

inspec_num =  330100141809180494

# sample_data = sample_data.set_index("每次检验编号")
# inspec_num = sys.argv[1]
slice_df = sample_data[(sample_data["每次检验编号"]==inspec_num)]
# slice_df

x = range(1,195)
y1 = slice_df['逐秒车速']
y2 = slice_df['逐秒CO浓度']
y2_100 = (y2* 100).tolist() #将CO的数据乘以100再绘图

y3 = slice_df['逐秒NO浓度']
y3_0p1 = (y3*0.1).tolist() #将NO的数据乘以0.1再绘图

y4 = slice_df['逐秒HC浓度']

# y5 = slice_df['vsp_bin']

fig, ax = plt.subplots(figsize = [20,10])
line1, = ax.plot(x, y1, 'black', linewidth=2.5, label='V km/h')
line2, = ax.plot(x, y2_100, 'orange', linewidth=2.5, label='CO $10^{-4}$')
line3, = ax.plot(x, y3_0p1, 'deepskyblue', linewidth=2.5, label='NO $10^{-5}$')
line4, = ax.plot(x, y4, 'red', linewidth=2.5, label='HC $10^{-6}$')
# line5, = ax.plot(x, y5, 'lightgreen', linewidth=2.5, label='vsp_bin')
ax.legend(loc='upper center',bbox_to_anchor=(0.6,0.95))
font1 = {'family': 'Times New Roman','weight': 'normal','size': 20,}  #图例的字体设置,prop参数适用于plt.legend
plt.legend(prop = font1)

x_tic = [0,11,15,23,28,49,61,85,96,117,143,155,163,176,195]
ax.xaxis.set_ticks(x_tic)
ax.set_xticklabels(x_tic,size = 16)
ax.tick_params(direction='in',width=2,length=6)
y_tic = range(0,80,10)
# y_tic = [0,10,20,30,40,50,60]
ax.yaxis.set_ticks(y_tic)
ax.set_yticklabels(y_tic,size = 20)

plt.xlabel('time (s)',fontsize=22)
plt.ylabel('V, CO, NO, HC',fontsize=22)
title = "Inspection number "+str(inspec_num)
plt.title(title,fontsize=25,verticalalignment='bottom')

ax=plt.gca()#获得坐标轴的句柄
width_x = 2.5
ax.spines['bottom'].set_linewidth(width_x)###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(width_x)####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(width_x)###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(width_x)###设置上边坐标轴的粗细

out_name = str(inspec_num)+'.png'

outpath = r"D:\Study\vehicle\test_line\0718"
outfile = os.path.join(outpath,out_name)
plt.savefig(outfile)
# plt.show()
# print(slice_df)
# ave = sample_data.mean()
