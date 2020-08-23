import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import linear_model

vel_path = r"D:\Study\vehicle\data"
inspec_file = r"sample_data.csv"
inspec_data = os.path.join(vel_path, inspec_file)
sample_data = pd.read_csv(inspec_data)
sample_data =sample_data.drop(["Unnamed: 0"],axis=1)
sample_data =sample_data.drop(["Unnamed: 0.1"],axis=1)
sample_data = sample_data.set_index("每次检验编号")

#年检数据
# sample_data["车龄"] = pd.to_datetime(sample_data['SXKSSJ'])-pd.to_datetime(sample_data['车辆登记时间'])

# sample_data["HC排放值"][sample_data.HC排放值>15]=np.nan
# sample_data["发动机排量"][sample_data.发动机排量>10000]=np.nan
# sample_data["累积行驶里程"][sample_data.累积行驶里程>1200000]=np.nan

# sample_data.dropna(inplace=True)

# sample_data.head(10).to_csv("head10.csv")
# print(sample_data["车龄"])
#
x = np.array(sample_data["加速度"]).reshape(-1,1)
y = np.array(sample_data["逐秒NO浓度"]).reshape(-1,1)
#
# # print(y.isnull().any())  # 判断有无缺失值,返回True or False
# # print(np.isnan(y).any()) # 判断有无NaN,返回True or False
#
# # # 输出回归分析的结果
model=linear_model.LinearRegression()
model.fit(x,y)
a=model.coef_ #获取自变量系数
a =round(float(a),5) # a与b都是ndarray类型，并非float
b= model.intercept_#获取截距
b =round(float(b),3)
R2=model.score(x,y) #R的平方
R2 = round(R2,5)

y1 = model.predict(x)
plt.plot(x,y1,color='blue',linewidth=1)

equation = 'y={}*x+{}   R2={}'.format(a, b, R2)
# print('线性回归方程为：','\n',equation)
# print('R2：','\n',R2)

# # 画散点图
plt.scatter(x, y, s=8, c= "red", alpha=0.5, marker="o",label=equation)
plt.legend()
plt.xlabel('accelerated speed',fontsize=15)
plt.ylabel('NO',fontsize=15)
title = "NO-accelerated speed"
plt.title(title,fontsize=20,verticalalignment='bottom')
plt.savefig("NO-accelerate-second_SCAT.png")
#
# ## plt.show()