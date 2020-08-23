import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import sys,glob


####把相同指标的统计文件合并为一个csv

path = r"D:\Study\vehicle\speed"
cols_list = ["逐秒NO浓度","逐秒CO浓度","逐秒HC浓度"]
# writer = pd.ExcelWriter('D:\ZJU\选调相关\统计\汇总.xlsx')
for col in cols_list:
    #
    all_files = glob.glob(os.path.join(path,(col+'*'+'.csv')))
    for i in range(len(all_files)):

        if i == 0:

            df = pd.read_csv(all_files[i])
        else:

            temp_df = pd.read_csv(all_files[i])

            df = pd.concat([df, temp_df])
    outname = col+"分车速"+".csv"
    df.to_csv(os.path.join(path,outname), encoding='utf_8_sig',index=None)

#
# ##选调结果csv文件汇总至Excel中
# path = r"C:\Users\1\PycharmProjects\dataframe"
# # file_list = [nList for nList in os.listdir(path) if nList[-3:]=="csv"]
# # # writer = pd.ExcelWriter('D:\ZJU\选调相关\统计\汇总.xlsx')
# # for file in file_list:
# with pd.ExcelWriter('D:\ZJU\选调相关\统计\汇总2.xlsx') as writer:
#     df_1 =pd.read_csv("D:\ZJU\选调相关\统计\毕业院校.csv").T
#
#     df_1.to_excel(writer, sheet_name= "毕业院校")
#     df_2 = pd.read_csv("D:\ZJU\选调相关\统计\专业.csv").T
#     df_2.to_excel(writer, sheet_name= "专业")
#     df_3 =pd.read_csv("D:\ZJU\选调相关\统计\民族.csv").T
#     df_3.to_excel(writer, sheet_name= "民族")
#     df_4 = pd.read_csv("D:\ZJU\选调相关\统计\选调地区.csv").T
#     df_4.to_excel(writer, sheet_name= "选调地区")
#     df_5 =pd.read_csv("D:\ZJU\选调相关\统计\性别.csv").T
#     df_5.to_excel(writer, sheet_name= "性别")
#     df_6 = pd.read_csv("D:\ZJU\选调相关\统计\学历.csv").T
#     df_6.to_excel(writer, sheet_name= "学历")
#
# writer.save()



##以下写法会导致sheet被后加入的sheet覆盖，原因待查
# for file in file_list:
#     df = pd.read_csv(file)
#     df.to_excel(writer,sheet_name = file[:-4])
#     writer.save()