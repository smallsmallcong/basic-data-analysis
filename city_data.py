#-*-coding:utf-8 -*-

#Xue Chen
#2020.3.6
#group obs_data by cityname

import pandas as pd
#import pinyin
import datetime
 
rawData = pd.read_csv('C:\Users\1\PycharmProjects\dataframe\all_191220-30.csv')
print (rawData) 
#去除重复值
ind_frame = rawData.drop_duplicates(keep='first')
city_list = ["北京", "杭州", "合肥", "济南", "南京","上海", "石家庄", "天津", "太原"]

for city in city_list:
    cityData = rawData[["date", "hour", "type", "city"]]
   # filename = pinyin.get(city, format = 'strip', delimiter = "")
    filename = city +'.csv'
cityData.to_csv(filename, index = False)

