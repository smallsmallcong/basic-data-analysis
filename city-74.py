#-*-coding:utf-8 -*-

#Xue Chen
#2020.8.21
#select obs_data of specific time period
#calculate average value of multi-sites
import pandas as pd
import numpy as np
import csv
import os,sys

path = r"D:\ZJU"
datapath = r"D:\ZJU\test"
bj = r"beijing.csv"
time = r"time.csv"
outpath = r"D:\ZJU\out"
time_list=pd.read_csv(os.path.join(path,time))
time_list["time"]= pd.to_datetime(time_list["time"], format='%Y-%m-%d %H:%M')
# BJ = os.path.join(path,file)
nameList = [nList for nList in os.listdir(datapath) if nList[-3:]=='csv']
# print(nameList)
#
for filename in nameList:
    outfile = filename
    file = os.path.join(datapath,filename)
    rawdata = pd.read_csv(file,header=None,names=['time','city','station','pm25','pm10','so2','no2','o3','o3_8'])
    rawdata.drop_duplicates(keep="first")
    ozonedata = rawdata.loc[:,['time','o3']]
    ozonedata["time"] = pd.to_datetime(ozonedata["time"], format='%Y-%m-%d %H:%M:%S')
    for i in range(len(time_list)):
        time_i = time_list.loc[i,"time"]
        time_list.loc[i,'o3'] = ozonedata['o3'][ozonedata.time==time_i].mean()
    time_list["h"] = time_list['time'].dt.hour
    tempData = time_list[ (time_list.h >=11) & (16>= time_list.h)]
    tempData.to_csv(os.path.join(outpath ,outfile),  columns =['time','o3'],index=False, encoding='utf_8_sig')