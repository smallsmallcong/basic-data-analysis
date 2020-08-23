#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt
import base

vel_path = r"D:\Study\vehicle\data\result-detail"
vel_path2 = r"D:\Study\vehicle\data\period"
outpath = r"D:\Study\vehicle\test_scat\不同排放阶段"
detail_file = r"vel_detail.csv"
# oil_file = r"oil_consume.csv"
vel_detail = pd.read_csv(os.path.join(vel_path, detail_file),low_memory=False)
# oil = pd.read_csv(os.path.join(vel_path, oil_file),encoding='gb18030') ##,low_memory=False ,encoding='unicode_escape'
# print(len(vel_detail))
#
emis_list = ["国1","国2","国3","国3带OBD","国4","国4(京5)","国5","国6"]
# percentile = [0.01,0.05,0.10,0.50,0.90,0.95,0.99]
# index_list = ["count","mean","std","min","1%","5%","10%","50%","90%","95%","99%","max"]
# # cols1 = ["HC排放值","CO排放值","NOx排放值","累积行驶里程","排量（L）"]
# cols2 = ["综合工况油耗","市区工况油耗","市郊工况油耗"] ##,

# print(vel_detail["座位数"])

# ###筛选检测合格的进行分析
# vel_detail=vel_detail[vel_detail.尾气检测合格与否==1]

vel_detail.loc[:,np.array(["整备/总质量（KG）","功率（KW）"])].to_csv("M-K2.csv")

# vel_detail.loc[:,"每次检验编号","整备/总质量（KG）","功率（KW）"].to_csv("M-K.csv")

###添加由质量和功率计算出的VSP的一列
# vel_detail["vsp_M/K"] = vel_detail["整备/总质量（KG）"]/vel_
# detail["功率（KW）"]
# print(vel_detail["功率（KW）"])

# ###去除排放标准为空白的行
# # print(len(vel_detail))
# vel_detail= vel_detail.dropna(axis = 0,subset = ['排放标准'])
# print(len(vel_detail))


##转换类型 用以下方法字符类型的数字依然未能完全转换为浮点数，原因待查
# for coli in cols2:
# #     # vel_detail[coli]=vel_detail[coli].fillna(" ").astype(np.float32)
# #     vel_detail[coli] = vel_detail[coli].apply(lambda x: " " if type(x)==str else x)
# #     vel_detail[coli]= [map(eval,x)  for x in vel_detail[coli]]
# #     ##float(x)
# #     # vel_detail[coli] = vel_detail[coli].apply(lambda x: " " if x== "NaN" else float(x))
# #
#     city_oil = vel_detail.loc[:,coli].tolist()
# # city_oil = [1.1,2.5,4,"3.2"]
#     for i in range(len(city_oil)):
#     # city_oil[i]= map(eval,city_oil[i])
#         if "/" in str(city_oil[i]):
#             city_oil[i]=" "
#         elif "-" in str(city_oil[i]):
#             city_oil[i] = " "
#         elif "L" in str(city_oil[i]):
#             city_oil[i] = " "
#         elif "a" in str(city_oil[i]):
#             city_oil[i] = " "
#         else:
#             city_oil[i] = float(city_oil[i]) ## map(eval,city_oil[i])
# # city_oil = [map(eval,x) for x in city_oil ]
#     city_oil = pd.DataFrame(city_oil,index= None)
#     print(city_oil)
#     print(city_oil.dtypes)

###绘制根据排放标准分形状和颜色的散点图
# NOx = vel_detail.loc[0:20000,"NOx排放值"]
# # CO = np.array(vel_detail["CO排放值"]).reshape(-1,1)
# HC = vel_detail.loc[0:20000,"HC排放值"]
# Classes = vel_detail.loc[0:20000,"排放标准"]##[(vel_detail.排放标准.notnull) & (vel_detail.排放标准 != "")]
# m = {"国1": 'o', "国2":"<", "国3":"s", "国3带OBD": 'D', "国4": '+',"国4(京5)":">","国5":"*","国6":"."}
# rs = {"国1": 'black', "国2":"lightblue", "国3":"brown", "国3带OBD": 'purple', "国4": 'orange',"国4(京5)":"pink","国5":"green","国6":"grey"}
# colors = list(map(lambda x: rs[x], Classes)) # 将相应的标签改为对应的颜色
# cm = list(map(lambda x: m[x], Classes))  # 将相应的标签改为对应的marker
# fig, ax = plt.subplots()
# scatter = base.mscatter(HC, NOx, c=colors, m=cm, ax=ax, cmap=plt.cm.RdYlBu)
# plt.xlim(0, 6)
# plt.ylim(0, 6)
# plt.xlabel('HC', fontsize=15)
# plt.ylabel('NOx', fontsize=15)
# title = "HC-NOx"
# plt.title(title, fontsize=20, verticalalignment='bottom')
#
# ###如何添加图例？待探究
# # produce a legend with the unique colors from the scatter
# # legend1 = ax.legend(*scatter.legend_elements(),
# #                     loc="lower left", title="Classes")
# # ax.add_artist(legend1)
# # # produce a legend with a cross section of sizes from the scatter
# # handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
# # legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")
# # plt.show()
# plt.savefig("NOx-HC-6.PNG")

###分排放阶段绘制污染物两两之间的散点图
# i = 6
# for i in range(len(emis_list)):
# while i < len(emis_list):
#     # emis = emis_list[i]
# NOx = np.array(vel_detail["NOx排放值"]).reshape(-1,1) ###[vel_detail.排放标准==emis_list[i]])
# # CO = np.array(vel_detail["CO排放值"]).reshape(-1,1) ##[vel_detail.排放标准==emis_list[i]]
# n = len(NOx)
# HC = np.array(vel_detail["HC排放值"]).reshape(-1,1) ##[vel_detail.排放标准==emis_list[i]]
# plt.scatter(HC,NOx, s=8, c="red", alpha=0.5, marker="o")
# # plt.legend()
# plt.xlabel('HC', fontsize=15)
# plt.ylabel('NOx', fontsize=15)
# title = "all_HC-NOx"+ "  n ="+str(n)
# plt.title(title, fontsize=20, verticalalignment='bottom')
# outname = "all_HC-NOx.png"
# plt.savefig(os.path.join(outpath,outname))
#     # i = i+1


##统计每种排放阶段污染物排放因子和油耗的分布情况
# for emis in emis_list:
#     for col in cols2:
#         df_slice = oil[col][oil.排放标准==emis]
#         emis_stat = df_slice.describe(percentiles=percentile)
#         emis_stat = pd.DataFrame(emis_stat, index=index_list).T
#         emis_stat =emis_stat.rename(index = {col:emis})
#         outname = str(emis)+"_"+str(col)+".csv"
#         outfile = os.path.join(vel_path2,outname)
#         emis_stat.to_csv(outfile)
#

##统计每列的各个元素出现的次数
# cols_list = ["排放标准"]
# for col in cols_list:
#     list1 = vel_detail[col].tolist()
#     a = base.all_list(list1)
#     stat = pd.DataFrame(a, index=[col])
#     outname = str(col) + "-2.csv"
#     stat.to_csv(outname)