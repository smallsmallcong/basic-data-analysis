import pandas as pd
import numpy as np
import os,sys

#根据设定的RH范围，对臭氧的分布进行描述统计；根据臭氧的范围，对RH的分布进行描述统计

path = r"D:\Study\筛选"
city_list =  [nList for nList in os.listdir(path) if nList[-3:]=='csv']
for file in city_list:
    outname = file[:-4]
    rawdata = pd.read_csv(os.path.join(path, file))
    rawdata = rawdata.set_index("time")
    O3_slice = rawdata["o3"][rawdata.humidity>=75]
    RH_slice = rawdata["humidity"][rawdata.o3>=200]
    percentile = [0.10,0.50,0.90]
    stat_O3 = O3_slice.describe(percentiles=percentile)
    stat_RH = RH_slice.describe(percentiles=percentile)
    index_list = ["count","mean","std","min","10%","50%","90%","max"]
    stat_O3 = pd.DataFrame(stat_O3,index=index_list).T
    stat_RH = pd.DataFrame(stat_RH,index=index_list).T   #转置
    stat_RH= stat_RH.rename(index={'humidity':outname})  #修改index为对应城市名
    stat_O3 = stat_O3.rename(index={'o3': outname})

    # print(stat_O3)


    stat_RH.to_csv (str(outname)+"_RH.csv")
    stat_O3.to_csv(str(outname)+"_O3.csv")
