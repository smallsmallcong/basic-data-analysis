import pandas as pd
import numpy as np
import os

work_path = r"D:\Study\萧山机动车\年检数据"
vel_path = r"D:\Study\vehicle"
work_file = r"WorkingState.csv"
vel_file = r"vel_data.csv"

workfile = os.path.join(work_path, work_file)
velfile = os.path.join(vel_path, vel_file)
workdata = pd.read_csv(workfile)
vel_data = pd.read_csv(velfile)
vel_all = pd.merge(workdata,vel_data,on = "每次检验编号", how = 'inner')
vel_all.to_csv("vel_all.csv",encoding='utf-8')