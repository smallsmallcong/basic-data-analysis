import pandas as pd
import numpy as np
import os

vel_path = r"D:\Study\vehicle"
vel_file = r"vel_all.csv"
all_data = os.path.join(vel_path, vel_file)
sample_data = pd.read_csv(all_data, nrows=97500)
sample_data.to_csv("sample_data.csv",encoding='utf-8', index=False)
