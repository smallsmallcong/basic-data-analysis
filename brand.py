import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt

vel_path = r"D:\Study\萧山机动车\年检数据"
inspec_file = r"vel.csv"
inspec_data = os.path.join(vel_path, inspec_file)
sample_data = pd.read_csv(inspec_data)
# sample_data =sample_data.drop(["Unnamed: 0"],axis=1)
# sample_data = sample_data.set_index("每次检验编号")
stat= sample_data.describe()
stat.to_csv("brand_stat.csv")

