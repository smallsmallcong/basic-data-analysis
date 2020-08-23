#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt
import base

vel_path = r"D:\Study\vehicle\data"
vel_path2 = r"D:\Study\vehicle\data\period"
detail_file = r"vel_detail.csv"
vel_detail = pd.read_csv(os.path.join(vel_path, detail_file),low_memory=False)
# print(len(vel_detail))

emis_list = ["国1","国2","国3","国3带OBD","国4","国4(京5)","国5","国6"]
percentile = [0.01,0.05,0.10,0.50,0.90,0.95,0.99]
index_list = ["count","mean","std","min","1%","5%","10%","50%","90%","95%","99%","max"]
cols1 = ["HC排放值","CO排放值","NOx排放值","累积行驶里程","排量（L）"]
cols2 = ["综合工况油耗","市区工况油耗","市郊工况油耗"]

# print(len(vel_detail))
##转换类型
for coli in cols2:
    city_oil = vel_detail.loc[:,coli].tolist()
    for i in range(len(city_oil)):
    # city_oil[i]= map(eval,city_oil[i])
        if "/" in str(city_oil[i]):
            city_oil[i]=" "
        elif "-" in str(city_oil[i]):
            city_oil[i] = " "
        elif "L" in str(city_oil[i]):
            city_oil[i] = " "
        elif "a" in str(city_oil[i]):
            city_oil[i] = " "
        else:
            city_oil[i] = float(city_oil[i]) ## map(eval,city_oil[i])
# city_oil = [map(eval,x) for x in city_oil ]
    vel_detail.loc[:, coli]= pd.Series(city_oil)
    # city_oil = pd.DataFrame(city_oil,index= None)
    # print(city_oil)
    # print(city_oil.dtypes)
print(vel_detail["综合工况油耗"])