import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import sys

path = r"D:\ZJU\选调相关"
file = r"四川省2016-2020年紧缺汇总.xlsx"

#统计列表中每个元素出现的次数，返回的是一个字典：{元素：次数}
def all_list(list1):
    result = {}
    for i in set(list1):
        result[i]=list1.count(i)
    return result

year_list = ["2016","2017","2018","2019","2020"]

cols_list = ["毕业院校","学历","专业","性别","民族","选调地区"]
for year in year_list:
    sc_xd = pd.read_excel((os.path.join(path, file)),sheet_name= year)
    sc_xd.set_index("序号")
    for col in cols_list:
        list1=sc_xd[col].tolist()
        a = all_list(list1)
        stat = pd.DataFrame(a,index=[year])
        outname = str(year)+"-"+str(col)+".csv"

        stat.to_csv(outname)

        # print(stat)
# print(sc_xd.head(10))