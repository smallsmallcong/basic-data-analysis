import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


s1 = pd.Series(np.random.randn(1000)) # 生成1000个点的符合正态分布的随机数
fig_dims = (7.5, 4)
fig, ax = plt.subplots(figsize=fig_dims)

fig = sns.distplot(s1,hist=True,kde=True,rug=True) # 前两个默认就是True,rug是在最下方显示出频率情况，默认为False
# bins=20 表示等分为20份的效果，同样有label等等参数
# sns.kdeplot(s1,shade=True,color='r') # shade表示线下颜色为阴影,color表示颜色是红色
# sns.rugplot(s1) # 在下方画出频率情况

histplot = fig.get_figure()
histplot.savefig("hist_a.png")
