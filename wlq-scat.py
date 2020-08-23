import pandas as pd
import matplotlib.pyplot as plt
import math
from statsmodels.formula.api import ols
from matplotlib.gridspec import GridSpec
from sklearn import linear_model
import sys
from matplotlib.pyplot import MultipleLocator
#WLQ
#scatter plot

path = '/public/home/wangliqiang/program/lmy3/data/merge/'

fig = plt.figure(1)
fig.set_size_inches(18.5,27.75)
gs = GridSpec(6,6)

###fig1
file1 = pd.read_csv(path+'changzhou.csv')

x1 = pd.DataFrame(file1['humidity'])
y1 = file1['o3']

trend1 = linear_model.LinearRegression()
trend1.fit(x1,y1)

y_pred1 = trend1.predict(x1)

ax1 = plt.subplot(gs[0,0])

ax1.set_xlim(0,100)
ax1.set_ylim(0,300)
x1_major_locator=MultipleLocator(25)
y1_major_locator=MultipleLocator(50)

ax1.scatter(x1,y1,color='red')
ax1.plot(x1,y_pred1,color='blue',linewidth=3)

#ax1.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax1.tick_params(labelsize=20)
#ax1.set_xlabel('RH (%)',fontsize=30, labelpad=0)

ax1.annotate('changzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax1.xaxis.set_major_locator(x1_major_locator)
ax1.yaxis.set_major_locator(y1_major_locator)
ax1.xaxis.set_major_formatter(plt.NullFormatter())
#ax1.yaxis.set_major_formatter(plt.NullFormatter())

coef1 = trend1.coef_
root1 = math.sqrt(trend1.score(x1,y1))

coef1 = str(round(float(coef1),2))
root1 = str(round(root1,2))

if float(coef1) < 0:

    formula1 = 'S'+'='+coef1+' '+'R'+'='+root1

else:

    formula1 = 'S'+'='+'+'+coef1+' '+'R'+'='+root1


ax1.annotate(formula1, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')


###fig2
file2 = pd.read_csv(path+'fuzhou.csv')

x2 = pd.DataFrame(file2['humidity'])
y2 = file2['o3']

trend2 = linear_model.LinearRegression()
trend2.fit(x2,y2)

y_pred2 = trend2.predict(x2)

ax2 = plt.subplot(gs[0,1])

ax2.set_xlim(0,100)
ax2.set_ylim(0,300)
x2_major_locator=MultipleLocator(25)
y2_major_locator=MultipleLocator(50)

ax2.scatter(x2,y2,color='red')
ax2.plot(x2,y_pred2,color='blue',linewidth=3)
ax2.tick_params(labelsize=20)

ax2.annotate('fuzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax2.xaxis.set_major_formatter(plt.NullFormatter())
ax2.yaxis.set_major_formatter(plt.NullFormatter())
ax2.xaxis.set_major_locator(x2_major_locator)
ax2.yaxis.set_major_locator(y2_major_locator)

coef2 = trend2.coef_
root2 = math.sqrt(trend2.score(x2,y2))

coef2 = str(round(float(coef2),2))
root2 = str(round(root2,2))

if float(coef2) < 0:

    formula2 = 'S'+'='+coef2+' '+'R'+'='+root2

else:

    formula2 = 'S'+'='+'+'+coef2+' '+'R'+'='+root2


ax2.annotate(formula2, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig3
file3 = pd.read_csv(path+'hangzhou.csv')

x3 = pd.DataFrame(file3['humidity'])
y3 = file3['o3']

trend3 = linear_model.LinearRegression()
trend3.fit(x3,y3)

y_pred3 = trend3.predict(x3)

ax3 = plt.subplot(gs[0,2])

ax3.set_xlim(0,100)
ax3.set_ylim(0,300)
x3_major_locator=MultipleLocator(25)
y3_major_locator=MultipleLocator(50)

ax3.scatter(x3,y3,color='red')
ax3.plot(x3,y_pred3,color='blue',linewidth=3)

#ax3.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax3.tick_params(labelsize=20)

ax3.annotate('hangzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax3.xaxis.set_major_formatter(plt.NullFormatter())
ax3.yaxis.set_major_formatter(plt.NullFormatter())
ax3.xaxis.set_major_locator(x3_major_locator)
ax3.yaxis.set_major_locator(y3_major_locator)

coef3 = trend3.coef_
root3 = math.sqrt(trend3.score(x3,y3))

coef3 = str(round(float(coef3),2))
root3 = str(round(root3,2))

if float(coef3) < 0:

    formula3 = 'S'+'='+coef3+' '+'R'+'='+root3

else:

    formula3 = 'S'+'='+'+'+coef3+' '+'R'+'='+root3


ax3.annotate(formula3, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig4
file4 = pd.read_csv(path+'hefei.csv')

x4 = pd.DataFrame(file4['humidity'])
y4 = file4['o3']

trend4 = linear_model.LinearRegression()
trend4.fit(x4,y4)

y_pred4 = trend4.predict(x4)

ax4 = plt.subplot(gs[0,3])

ax4.set_xlim(0,100)
ax4.set_ylim(0,300)
x4_major_locator=MultipleLocator(25)
y4_major_locator=MultipleLocator(50)

ax4.scatter(x4,y4,color='red')
ax4.plot(x4,y_pred4,color='blue',linewidth=3)
ax4.tick_params(labelsize=20)

ax4.annotate('hefei', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax4.xaxis.set_major_formatter(plt.NullFormatter())
ax4.yaxis.set_major_formatter(plt.NullFormatter())
ax4.xaxis.set_major_locator(x4_major_locator)
ax4.yaxis.set_major_locator(y4_major_locator)

coef4 = trend4.coef_
root4 = math.sqrt(trend4.score(x4,y4))

coef4 = str(round(float(coef4),2))
root4 = str(round(root4,2))

if float(coef4) < 0:

    formula4 = 'S'+'='+coef4+' '+'R'+'='+root4

else:

    formula4 = 'S'+'='+'+'+coef4+' '+'R'+'='+root4


ax4.annotate(formula4, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig5
file5 = pd.read_csv(path+'huaian.csv')

x5 = pd.DataFrame(file5['humidity'])
y5 = file5['o3']

trend5 = linear_model.LinearRegression()
trend5.fit(x5,y5)

y_pred5 = trend5.predict(x5)

ax5 = plt.subplot(gs[0,4])

ax5.set_xlim(0,100)
ax5.set_ylim(0,300)
x5_major_locator=MultipleLocator(25)
y5_major_locator=MultipleLocator(50)

ax5.scatter(x5,y5,color='red')
ax5.plot(x5,y_pred5,color='blue',linewidth=3)

#ax5.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax5.tick_params(labelsize=20)

ax5.annotate('huaian', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax5.xaxis.set_major_formatter(plt.NullFormatter())
ax5.yaxis.set_major_formatter(plt.NullFormatter())
ax5.xaxis.set_major_locator(x5_major_locator)
ax5.yaxis.set_major_locator(y5_major_locator)

coef5 = trend5.coef_
root5 = math.sqrt(trend5.score(x5,y5))

coef5 = str(round(float(coef5),2))
root5 = str(round(root5,2))

if float(coef5) < 0:

    formula5 = 'S'+'='+coef5+' '+'R'+'='+root5

else:

    formula5 = 'S'+'='+'+'+coef5+' '+'R'+'='+root5


ax5.annotate(formula5, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig6
file6 = pd.read_csv(path+'huzhou.csv')

x6 = pd.DataFrame(file6['humidity'])
y6 = file6['o3']

trend6 = linear_model.LinearRegression()
trend6.fit(x6,y6)

y_pred6 = trend6.predict(x6)

ax6 = plt.subplot(gs[0,5])

ax6.set_xlim(0,100)
ax6.set_ylim(0,300)
x6_major_locator=MultipleLocator(25)
y6_major_locator=MultipleLocator(50)

ax6.scatter(x6,y6,color='red')
ax6.plot(x6,y_pred6,color='blue',linewidth=3)

ax6.annotate('huzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax6.xaxis.set_major_formatter(plt.NullFormatter())
ax6.yaxis.set_major_formatter(plt.NullFormatter())
ax6.xaxis.set_major_locator(x6_major_locator)
ax6.yaxis.set_major_locator(y6_major_locator)

coef6 = trend6.coef_
root6 = math.sqrt(trend6.score(x6,y6))

coef6 = str(round(float(coef6),2))
root6 = str(round(root6,2))

if float(coef6) < 0:

    formula6 = 'S'+'='+coef6+' '+'R'+'='+root6

else:

    formula6 = 'S'+'='+'+'+coef6+' '+'R'+'='+root6


ax6.annotate(formula6, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig7
file7 = pd.read_csv(path+'jiaxing.csv')

x7 = pd.DataFrame(file7['humidity'])
y7 = file7['o3']

trend7 = linear_model.LinearRegression()
trend7.fit(x7,y7)

y_pred7 = trend7.predict(x7)

ax7 = plt.subplot(gs[1,0])

ax7.set_xlim(0,100)
ax7.set_ylim(0,300)
x7_major_locator=MultipleLocator(25)
y7_major_locator=MultipleLocator(50)

ax7.scatter(x7,y7,color='red')
ax7.plot(x7,y_pred7,color='blue',linewidth=3)

#ax7.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax7.tick_params(labelsize=20)

ax7.annotate('jiaxing', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')
#ax7.yaxis.set_major_formatter(plt.NullFormatter())
ax7.xaxis.set_major_formatter(plt.NullFormatter())
ax7.xaxis.set_major_locator(x7_major_locator)
ax7.yaxis.set_major_locator(y7_major_locator)

coef7 = trend7.coef_
root7 = math.sqrt(trend7.score(x7,y7))

coef7 = str(round(float(coef7),2))
root7 = str(round(root7,2))

if float(coef7) < 0:

    formula7 = 'S'+'='+coef7+' '+'R'+'='+root7

else:

    formula7 = 'S'+'='+'+'+coef7+' '+'R'+'='+root7


ax7.annotate(formula7, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig8
file8 = pd.read_csv(path+'jinan.csv')

x8 = pd.DataFrame(file8['humidity'])
y8 = file8['o3']

trend8 = linear_model.LinearRegression()
trend8.fit(x8,y8)

y_pred8 = trend8.predict(x8)

ax8 = plt.subplot(gs[1,1])

ax8.set_xlim(0,100)
ax8.set_ylim(0,300)
x8_major_locator=MultipleLocator(25)
y8_major_locator=MultipleLocator(50)

ax8.scatter(x8,y8,color='red')
ax8.plot(x8,y_pred8,color='blue',linewidth=3)

ax8.annotate('jinan', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax8.xaxis.set_major_formatter(plt.NullFormatter())
ax8.yaxis.set_major_formatter(plt.NullFormatter())
ax8.xaxis.set_major_locator(x8_major_locator)
ax8.yaxis.set_major_locator(y8_major_locator)

coef8 = trend8.coef_
root8 = math.sqrt(trend8.score(x8,y8))

coef8 = str(round(float(coef8),2))
root8 = str(round(root8,2))

if float(coef8) < 0:

    formula8 = 'S'+'='+coef8+' '+'R'+'='+root8

else:

    formula8 = 'S'+'='+'+'+coef8+' '+'R'+'='+root8


ax8.annotate(formula8, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig9
file9 = pd.read_csv(path+'jinhua.csv')

x9 = pd.DataFrame(file9['humidity'])
y9 = file9['o3']

trend9 = linear_model.LinearRegression()
trend9.fit(x9,y9)

y_pred9 = trend9.predict(x9)

ax9 = plt.subplot(gs[1,2])

ax9.set_xlim(0,100)
ax9.set_ylim(0,300)
x9_major_locator=MultipleLocator(25)
y9_major_locator=MultipleLocator(50)

ax9.scatter(x9,y9,color='red')
ax9.plot(x9,y_pred9,color='blue',linewidth=3)

#ax9.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax9.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax9.tick_params(labelsize=20)

ax9.annotate('jinhua', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax9.xaxis.set_major_formatter(plt.NullFormatter())
ax9.yaxis.set_major_formatter(plt.NullFormatter())
ax9.xaxis.set_major_locator(x9_major_locator)
ax9.yaxis.set_major_locator(y9_major_locator)

coef9 = trend9.coef_
root9 = math.sqrt(trend9.score(x9,y9))

coef9 = str(round(float(coef9),2))
root9 = str(round(root9,2))

if float(coef9) < 0:

    formula9 = 'S'+'='+coef9+' '+'R'+'='+root9

else:

    formula9 = 'S'+'='+'+'+coef9+' '+'R'+'='+root9


ax9.annotate(formula9, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig10
file10 = pd.read_csv(path+'lianyungang.csv')

x10 = pd.DataFrame(file10['humidity'])
y10 = file10['o3']

trend10 = linear_model.LinearRegression()
trend10.fit(x10,y10)

y_pred10 = trend10.predict(x10)

ax10 = plt.subplot(gs[1,3])

ax10.set_xlim(0,100)
ax10.set_ylim(0,300)
x10_major_locator=MultipleLocator(25)
y10_major_locator=MultipleLocator(50)

ax10.scatter(x10,y10,color='red')
ax10.plot(x10,y_pred10,color='blue',linewidth=3)

#ax10.set_xlabel('RH (%)',fontsize=30, labelpad=0)
ax10.tick_params(labelsize=20)

ax10.annotate('lianyungang', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax10.xaxis.set_major_formatter(plt.NullFormatter())
ax10.yaxis.set_major_formatter(plt.NullFormatter())
ax10.xaxis.set_major_locator(x10_major_locator)
ax10.yaxis.set_major_locator(y10_major_locator)

coef10 = trend10.coef_
root10 = math.sqrt(trend10.score(x10,y10))

coef10 = str(round(float(coef10),2))
root10 = str(round(root10,2))

if float(coef10) < 0:

    formula10 = 'S'+'='+coef10+' '+'R'+'='+root10

else:

    formula10 = 'S'+'='+'+'+coef10+' '+'R'+'='+root10


ax10.annotate(formula10, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig11
file11 = pd.read_csv(path+'lishui.csv')

x11 = pd.DataFrame(file11['humidity'])
y11 = file11['o3']

trend11 = linear_model.LinearRegression()
trend11.fit(x11,y11)

y_pred11 = trend11.predict(x11)

ax11 = plt.subplot(gs[1,4])

ax11.set_xlim(0,100)
ax11.set_ylim(0,300)
x11_major_locator=MultipleLocator(25)
y11_major_locator=MultipleLocator(50)

ax11.scatter(x11,y11,color='red')
ax11.plot(x11,y_pred11,color='blue',linewidth=3)

#ax1.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax11.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax11.tick_params(labelsize=20)

ax11.annotate('lishui', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax11.xaxis.set_major_formatter(plt.NullFormatter())
ax11.yaxis.set_major_formatter(plt.NullFormatter())
ax11.xaxis.set_major_locator(x11_major_locator)
ax11.yaxis.set_major_locator(y11_major_locator)

coef11 = trend11.coef_
root11 = math.sqrt(trend11.score(x11,y11))

coef11 = str(round(float(coef11),2))
root11 = str(round(root11,2))

if float(coef11) < 0:

    formula11 = 'S'+'='+coef11+' '+'R'+'='+root11

else:

    formula11 = 'S'+'='+'+'+coef11+' '+'R'+'='+root11


ax11.annotate(formula11, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig12
file12 = pd.read_csv(path+'nanchang.csv')

x12 = pd.DataFrame(file12['humidity'])
y12 = file12['o3']

trend12 = linear_model.LinearRegression()
trend12.fit(x12,y12)

y_pred12 = trend12.predict(x12)

ax12 = plt.subplot(gs[1,5])

ax12.set_xlim(0,100)
ax12.set_ylim(0,300)
x12_major_locator=MultipleLocator(25)
y12_major_locator=MultipleLocator(50)

ax12.scatter(x12,y12,color='red')
ax12.plot(x12,y_pred12,color='blue',linewidth=3)

#ax12.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax12.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax12.tick_params(labelsize=20)

ax12.annotate('nanchang', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax12.xaxis.set_major_formatter(plt.NullFormatter())
ax12.yaxis.set_major_formatter(plt.NullFormatter())
ax12.xaxis.set_major_locator(x12_major_locator)
ax12.yaxis.set_major_locator(y12_major_locator)

coef12 = trend12.coef_
root12 = math.sqrt(trend12.score(x12,y12))

coef12 = str(round(float(coef12),2))
root12 = str(round(root12,2))

if float(coef12) < 0:

    formula12 = 'S'+'='+coef12+' '+'R'+'='+root12

else:

    formula12 = 'S'+'='+'+'+coef12+' '+'R'+'='+root12


ax12.annotate(formula12, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig13
file13 = pd.read_csv(path+'nanjing.csv')

x13 = pd.DataFrame(file13['humidity'])
y13 = file13['o3']

trend13 = linear_model.LinearRegression()
trend13.fit(x13,y13)

y_pred13 = trend13.predict(x13)

ax13 = plt.subplot(gs[2,0])

ax13.set_xlim(0,100)
ax13.set_ylim(0,300)
x13_major_locator=MultipleLocator(25)
y13_major_locator=MultipleLocator(50)

ax13.scatter(x13,y13,color='red')
ax13.plot(x13,y_pred13,color='blue',linewidth=3)

#ax13.set_xlabel('RH (%)',fontsize=30, labelpad=0)
ax13.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax13.tick_params(labelsize=20)

ax13.annotate('nanjing', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')
#ax13.yaxis.set_major_formatter(plt.NullFormatter())
ax13.xaxis.set_major_formatter(plt.NullFormatter())
ax13.xaxis.set_major_locator(x13_major_locator)
ax13.yaxis.set_major_locator(y13_major_locator)

coef13 = trend13.coef_
root13 = math.sqrt(trend13.score(x13,y13))

coef13 = str(round(float(coef13),2))
root13 = str(round(root13,2))

if float(coef13) < 0:

    formula13 = 'S'+'='+coef13+' '+'R'+'='+root13

else:

    formula13 = 'S'+'='+'+'+coef13+' '+'R'+'='+root13


ax13.annotate(formula13, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig14
file14 = pd.read_csv(path+'nantong.csv')

x14 = pd.DataFrame(file14['humidity'])
y14 = file14['o3']

trend14 = linear_model.LinearRegression()
trend14.fit(x14,y14)

y_pred14 = trend14.predict(x14)

ax14 = plt.subplot(gs[2,1])

ax14.set_xlim(0,100)
ax14.set_ylim(0,300)
x14_major_locator=MultipleLocator(25)
y14_major_locator=MultipleLocator(50)

ax14.scatter(x14,y14,color='red')
ax14.plot(x14,y_pred14,color='blue',linewidth=3)

#ax14.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax14.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax14.tick_params(labelsize=20)

ax14.annotate('nantong', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax14.xaxis.set_major_formatter(plt.NullFormatter())
ax14.yaxis.set_major_formatter(plt.NullFormatter())
ax14.xaxis.set_major_locator(x14_major_locator)
ax14.yaxis.set_major_locator(y14_major_locator)

coef14 = trend14.coef_
root14 = math.sqrt(trend14.score(x14,y14))

coef14 = str(round(float(coef14),2))
root14 = str(round(root14,2))

if float(coef14) < 0:

    formula14 = 'S'+'='+coef14+' '+'R'+'='+root14

else:

    formula14 = 'S'+'='+'+'+coef14+' '+'R'+'='+root14


ax14.annotate(formula14, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig15
file15 = pd.read_csv(path+'ningbo.csv')

x15 = pd.DataFrame(file15['humidity'])
y15 = file15['o3']

trend15 = linear_model.LinearRegression()
trend15.fit(x15,y15)

y_pred15 = trend15.predict(x15)

ax15 = plt.subplot(gs[2,2])

ax15.set_xlim(0,100)
ax15.set_ylim(0,300)
x15_major_locator=MultipleLocator(25)
y15_major_locator=MultipleLocator(50)

ax15.scatter(x15,y15,color='red')
ax15.plot(x15,y_pred15,color='blue',linewidth=3)

#ax15.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax15.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax15.tick_params(labelsize=20)

ax15.annotate('ningbo', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax15.xaxis.set_major_formatter(plt.NullFormatter())
ax15.yaxis.set_major_formatter(plt.NullFormatter())
ax15.xaxis.set_major_locator(x15_major_locator)
ax15.yaxis.set_major_locator(y15_major_locator)

coef15 = trend15.coef_
root15 = math.sqrt(trend15.score(x15,y15))

coef15 = str(round(float(coef15),2))
root15 = str(round(root15,2))

if float(coef15) < 0:

    formula15 = 'S'+'='+coef15+' '+'R'+'='+root15

else:

    formula15 = 'S'+'='+'+'+coef15+' '+'R'+'='+root15


ax15.annotate(formula15, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig16
file16 = pd.read_csv(path+'qingdao.csv')

x16 = pd.DataFrame(file16['humidity'])
y16 = file16['o3']

trend16 = linear_model.LinearRegression()
trend16.fit(x16,y16)

y_pred16 = trend16.predict(x16)

ax16 = plt.subplot(gs[2,3])

ax16.set_xlim(0,100)
ax16.set_ylim(0,300)
x16_major_locator=MultipleLocator(25)
y16_major_locator=MultipleLocator(50)

ax16.scatter(x16,y16,color='red')
ax16.plot(x16,y_pred16,color='blue',linewidth=3)

#ax16.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax16.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax16.tick_params(labelsize=20)

ax16.annotate('qingdao', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax16.xaxis.set_major_formatter(plt.NullFormatter())
ax16.yaxis.set_major_formatter(plt.NullFormatter())
ax16.xaxis.set_major_locator(x16_major_locator)
ax16.yaxis.set_major_locator(y16_major_locator)

coef16 = trend16.coef_
root16 = math.sqrt(trend16.score(x16,y16))

coef16 = str(round(float(coef16),2))
root16 = str(round(root16,2))

if float(coef16) < 0:

    formula16 = 'S'+'='+coef16+' '+'R'+'='+root16

else:

    formula16 = 'S'+'='+'+'+coef16+' '+'R'+'='+root16


ax16.annotate(formula16, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig17
file17 = pd.read_csv(path+'quzhou.csv')

x17 = pd.DataFrame(file17['humidity'])
y17 = file17['o3']

trend17 = linear_model.LinearRegression()
trend17.fit(x17,y17)

y_pred17 = trend17.predict(x17)

ax17 = plt.subplot(gs[2,4])

ax17.set_xlim(0,100)
ax17.set_ylim(0,300)
x17_major_locator=MultipleLocator(25)
y17_major_locator=MultipleLocator(50)

ax17.scatter(x17,y17,color='red')
ax17.plot(x17,y_pred17,color='blue',linewidth=3)

#ax17.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax17.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax17.tick_params(labelsize=20)

ax17.annotate('quzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax17.xaxis.set_major_formatter(plt.NullFormatter())
ax17.yaxis.set_major_formatter(plt.NullFormatter())
ax17.xaxis.set_major_locator(x17_major_locator)
ax17.yaxis.set_major_locator(y17_major_locator)

coef17 = trend17.coef_
root17 = math.sqrt(trend17.score(x17,y17))

coef17 = str(round(float(coef17),2))
root17 = str(round(root17,2))

if float(coef17) < 0:

    formula17 = 'S'+'='+coef17+' '+'R'+'='+root17

else:

    formula17 = 'S'+'='+'+'+coef17+' '+'R'+'='+root17


ax17.annotate(formula17, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig18
file18 = pd.read_csv(path+'shanghai.csv')

x18 = pd.DataFrame(file18['humidity'])
y18 = file18['o3']

trend18 = linear_model.LinearRegression()
trend18.fit(x18,y18)

y_pred18 = trend18.predict(x18)

ax18 = plt.subplot(gs[2,5])

ax18.set_xlim(0,100)
ax18.set_ylim(0,300)
x18_major_locator=MultipleLocator(25)
y18_major_locator=MultipleLocator(50)

ax18.scatter(x18,y18,color='red')
ax18.plot(x18,y_pred18,color='blue',linewidth=3)

#ax18.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax18.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax18.tick_params(labelsize=20)

ax18.annotate('shanghai', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax18.xaxis.set_major_formatter(plt.NullFormatter())
ax18.yaxis.set_major_formatter(plt.NullFormatter())
ax18.xaxis.set_major_locator(x18_major_locator)
ax18.yaxis.set_major_locator(y18_major_locator)

coef18 = trend18.coef_
root18 = math.sqrt(trend18.score(x18,y18))

coef18 = str(round(float(coef18),2))
root18 = str(round(root18,2))

if float(coef18) < 0:

    formula18 = 'S'+'='+coef18+' '+'R'+'='+root18

else:

    formula18 = 'S'+'='+'+'+coef18+' '+'R'+'='+root18


ax18.annotate(formula18, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig19
file19 = pd.read_csv(path+'shaoxing.csv')

x19 = pd.DataFrame(file19['humidity'])
y19 = file19['o3']

trend19 = linear_model.LinearRegression()
trend19.fit(x19,y19)

y_pred19 = trend19.predict(x19)

ax19 = plt.subplot(gs[3,0])

ax19.set_xlim(0,100)
ax19.set_ylim(0,300)
x19_major_locator=MultipleLocator(25)
y19_major_locator=MultipleLocator(50)

ax19.scatter(x19,y19,color='red')
ax19.plot(x19,y_pred19,color='blue',linewidth=3)

#ax19.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax19.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax19.tick_params(labelsize=20)

ax19.annotate('shaoxing', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax19.xaxis.set_major_formatter(plt.NullFormatter())
ax19.xaxis.set_major_locator(x19_major_locator)
ax19.yaxis.set_major_locator(y19_major_locator)

coef19 = trend19.coef_
root19 = math.sqrt(trend19.score(x19,y19))

coef19 = str(round(float(coef19),2))
root19 = str(round(root19,2))

if float(coef19) < 0:

    formula19 = 'S'+'='+coef19+' '+'R'+'='+root19

else:

    formula19 = 'S'+'='+'+'+coef19+' '+'R'+'='+root19


ax19.annotate(formula19, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig20
file20 = pd.read_csv(path+'suqian.csv')

x20 = pd.DataFrame(file20['humidity'])
y20 = file20['o3']

trend20 = linear_model.LinearRegression()
trend20.fit(x20,y20)

y_pred20 = trend20.predict(x20)

ax20 = plt.subplot(gs[3,1])

ax20.set_xlim(0,100)
ax20.set_ylim(0,300)
x20_major_locator=MultipleLocator(25)
y20_major_locator=MultipleLocator(50)

ax20.scatter(x20,y20,color='red')
ax20.plot(x20,y_pred20,color='blue',linewidth=3)

#ax20.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax20.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax20.tick_params(labelsize=20)

ax20.annotate('suqian', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax20.xaxis.set_major_formatter(plt.NullFormatter())
ax20.yaxis.set_major_formatter(plt.NullFormatter())
ax20.xaxis.set_major_locator(x20_major_locator)
ax20.yaxis.set_major_locator(y20_major_locator)

coef20 = trend20.coef_
root20 = math.sqrt(trend20.score(x20,y20))

coef20 = str(round(float(coef20),2))
root20 = str(round(root20,2))

if float(coef20) < 0:

    formula20 = 'S'+'='+coef20+' '+'R'+'='+root20

else:

    formula20 = 'S'+'='+'+'+coef20+' '+'R'+'='+root20


ax20.annotate(formula20, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig21
file21 = pd.read_csv(path+'suzhou.csv')

x21 = pd.DataFrame(file21['humidity'])
y21 = file21['o3']

trend21 = linear_model.LinearRegression()
trend21.fit(x21,y21)

y_pred21 = trend21.predict(x21)

ax21 = plt.subplot(gs[3,2])

ax21.set_xlim(0,100)
ax21.set_ylim(0,300)
x21_major_locator=MultipleLocator(25)
y21_major_locator=MultipleLocator(50)

ax21.scatter(x21,y21,color='red')
ax21.plot(x21,y_pred21,color='blue',linewidth=3)

#ax21.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax21.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax21.tick_params(labelsize=20)

ax21.annotate('suzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax21.xaxis.set_major_formatter(plt.NullFormatter())
ax21.yaxis.set_major_formatter(plt.NullFormatter())
ax21.xaxis.set_major_locator(x21_major_locator)
ax21.yaxis.set_major_locator(y21_major_locator)

coef21 = trend21.coef_
root21 = math.sqrt(trend21.score(x21,y21))

coef21 = str(round(float(coef21),2))
root21 = str(round(root21,2))

if float(coef21) < 0:

    formula21 = 'S'+'='+coef21+' '+'R'+'='+root21

else:

    formula21 = 'S'+'='+'+'+coef21+' '+'R'+'='+root21


ax21.annotate(formula21, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig22
file22 = pd.read_csv(path+'taizhouj.csv')

x22 = pd.DataFrame(file22['humidity'])
y22 = file22['o3']

trend22 = linear_model.LinearRegression()
trend22.fit(x22,y22)

y_pred22 = trend22.predict(x22)

ax22 = plt.subplot(gs[3,3])

ax22.set_xlim(0,100)
ax22.set_ylim(0,300)
x22_major_locator=MultipleLocator(25)
y22_major_locator=MultipleLocator(50)

ax22.scatter(x22,y22,color='red')
ax22.plot(x22,y_pred22,color='blue',linewidth=3)

#ax22.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax22.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax22.tick_params(labelsize=20)

ax22.annotate('taizhouj', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax22.xaxis.set_major_formatter(plt.NullFormatter())
ax22.yaxis.set_major_formatter(plt.NullFormatter())
ax22.xaxis.set_major_locator(x22_major_locator)
ax22.yaxis.set_major_locator(y22_major_locator)

coef22 = trend22.coef_
root22 = math.sqrt(trend22.score(x22,y22))

coef22 = str(round(float(coef22),2))
root22 = str(round(root22,2))

if float(coef22) < 0:

    formula22 = 'S'+'='+coef22+' '+'R'+'='+root22

else:

    formula22 = 'S'+'='+'+'+coef22+' '+'R'+'='+root22


ax22.annotate(formula22, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig23
file23 = pd.read_csv(path+'taizhouz.csv')

x23 = pd.DataFrame(file23['humidity'])
y23 = file23['o3']

trend23 = linear_model.LinearRegression()
trend23.fit(x23,y23)

y_pred23 = trend23.predict(x23)

ax23 = plt.subplot(gs[3,4])

ax23.set_xlim(0,100)
ax23.set_ylim(0,300)
x23_major_locator=MultipleLocator(25)
y23_major_locator=MultipleLocator(50)

ax23.scatter(x23,y23,color='red')
ax23.plot(x23,y_pred23,color='blue',linewidth=3)

#ax23.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax23.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax23.tick_params(labelsize=20)

ax23.annotate('taizhouz', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax23.xaxis.set_major_formatter(plt.NullFormatter())
ax23.yaxis.set_major_formatter(plt.NullFormatter())
ax23.xaxis.set_major_locator(x23_major_locator)
ax23.yaxis.set_major_locator(y23_major_locator)

coef23 = trend23.coef_
root23 = math.sqrt(trend23.score(x23,y23))

coef23 = str(round(float(coef23),2))
root23 = str(round(root23,2))

if float(coef23) < 0:

    formula23 = 'S'+'='+coef23+' '+'R'+'='+root23

else:

    formula23 = 'S'+'='+'+'+coef23+' '+'R'+'='+root23


ax23.annotate(formula23, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig24
file24 = pd.read_csv(path+'wenzhou.csv')

x24 = pd.DataFrame(file24['humidity'])
y24 = file24['o3']

trend24 = linear_model.LinearRegression()
trend24.fit(x24,y24)

y_pred24 = trend24.predict(x24)

ax24 = plt.subplot(gs[3,5])

ax24.set_xlim(0,100)
ax24.set_ylim(0,300)
x24_major_locator=MultipleLocator(25)
y24_major_locator=MultipleLocator(50)

ax24.scatter(x24,y24,color='red')
ax24.plot(x24,y_pred24,color='blue',linewidth=3)

#ax24.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax24.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax24.tick_params(labelsize=20)

ax24.annotate('wenzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax24.xaxis.set_major_formatter(plt.NullFormatter())
ax24.yaxis.set_major_formatter(plt.NullFormatter())
ax24.xaxis.set_major_locator(x24_major_locator)
ax24.yaxis.set_major_locator(y24_major_locator)

coef24 = trend24.coef_
root24 = math.sqrt(trend24.score(x24,y24))

coef24 = str(round(float(coef24),2))
root24 = str(round(root24,2))

if float(coef24) < 0:

    formula24 = 'S'+'='+coef24+' '+'R'+'='+root24

else:

    formula24 = 'S'+'='+'+'+coef24+' '+'R'+'='+root24


ax24.annotate(formula24, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig25
file25 = pd.read_csv(path+'wuxi.csv')

x25 = pd.DataFrame(file25['humidity'])
y25 = file25['o3']

trend25 = linear_model.LinearRegression()
trend25.fit(x25,y25)

y_pred25 = trend25.predict(x25)

ax25 = plt.subplot(gs[4,0])

ax25.set_xlim(0,100)
ax25.set_ylim(0,300)
x25_major_locator=MultipleLocator(25)
y25_major_locator=MultipleLocator(50)

ax25.scatter(x25,y25,color='red')
ax25.plot(x25,y_pred25,color='blue',linewidth=3)

#x25.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax25.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax25.tick_params(labelsize=20)

ax25.annotate('wuxi', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

ax25.xaxis.set_major_formatter(plt.NullFormatter())
ax25.xaxis.set_major_locator(x25_major_locator)
ax25.yaxis.set_major_locator(y25_major_locator)

coef25 = trend25.coef_
root25 = math.sqrt(trend25.score(x25,y25))

coef25 = str(round(float(coef25),2))
root25 = str(round(root25,2))

if float(coef25) < 0:

    formula25 = 'S'+'='+coef25+' '+'R'+'='+root25

else:

    formula25 = 'S'+'='+'+'+coef25+' '+'R'+'='+root25


ax25.annotate(formula25, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig26
file26 = pd.read_csv(path+'xiamen.csv')

x26 = pd.DataFrame(file26['humidity'])
y26 = file26['o3']

trend26 = linear_model.LinearRegression()
trend26.fit(x26,y26)

y_pred26 = trend26.predict(x26)

ax26 = plt.subplot(gs[4,1])

ax26.set_xlim(0,100)
ax26.set_ylim(0,300)
x26_major_locator=MultipleLocator(25)
y26_major_locator=MultipleLocator(50)

ax26.scatter(x26,y26,color='red')
ax26.plot(x26,y_pred26,color='blue',linewidth=3)

#ax26.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax26.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax26.tick_params(labelsize=20)

ax26.annotate('xiamen', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

#ax26.xaxis.set_major_formatter(plt.NullFormatter())
ax26.yaxis.set_major_formatter(plt.NullFormatter())
ax26.xaxis.set_major_locator(x26_major_locator)
ax26.yaxis.set_major_locator(y26_major_locator)

coef26 = trend26.coef_
root26 = math.sqrt(trend26.score(x26,y26))

coef26 = str(round(float(coef26),2))
root26 = str(round(root26,2))

if float(coef26) < 0:

    formula26 = 'S'+'='+coef26+' '+'R'+'='+root26

else:

    formula26 = 'S'+'='+'+'+coef26+' '+'R'+'='+root26


ax26.annotate(formula26, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig27
file27 = pd.read_csv(path+'xuzhou.csv')

x27 = pd.DataFrame(file27['humidity'])
y27 = file27['o3']

trend27 = linear_model.LinearRegression()
trend27.fit(x27,y27)

y_pred27 = trend27.predict(x27)

ax27 = plt.subplot(gs[4,2])

ax27.set_xlim(0,100)
ax27.set_ylim(0,300)
x27_major_locator=MultipleLocator(25)
y27_major_locator=MultipleLocator(50)

ax27.scatter(x27,y27,color='red')
ax27.plot(x27,y_pred27,color='blue',linewidth=3)

#ax27.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax27.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax27.tick_params(labelsize=20)

ax27.annotate('xuzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

#ax27.xaxis.set_major_formatter(plt.NullFormatter())
ax27.yaxis.set_major_formatter(plt.NullFormatter())
ax27.xaxis.set_major_locator(x27_major_locator)
ax27.yaxis.set_major_locator(y27_major_locator)

coef27 = trend27.coef_
root27 = math.sqrt(trend27.score(x27,y27))

coef27 = str(round(float(coef27),2))
root27 = str(round(root27,2))

if float(coef27) < 0:

    formula27 = 'S'+'='+coef27+' '+'R'+'='+root27

else:

    formula27 = 'S'+'='+'+'+coef27+' '+'R'+'='+root27


ax27.annotate(formula27, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig28
file28 = pd.read_csv(path+'yancheng.csv')

x28 = pd.DataFrame(file28['humidity'])
y28 = file28['o3']

trend28 = linear_model.LinearRegression()
trend28.fit(x28,y28)

y_pred28 = trend28.predict(x28)

ax28 = plt.subplot(gs[4,3])

ax28.set_xlim(0,100)
ax28.set_ylim(0,300)
x28_major_locator=MultipleLocator(25)
y28_major_locator=MultipleLocator(50)

ax28.scatter(x28,y28,color='red')
ax28.plot(x28,y_pred28,color='blue',linewidth=3)

#ax28.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax28.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax28.tick_params(labelsize=20)

ax28.annotate('yancheng', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

#ax28.xaxis.set_major_formatter(plt.NullFormatter())
ax28.yaxis.set_major_formatter(plt.NullFormatter())
ax28.xaxis.set_major_locator(x28_major_locator)
ax28.yaxis.set_major_locator(y28_major_locator)

coef28 = trend28.coef_
root28 = math.sqrt(trend28.score(x28,y28))

coef28 = str(round(float(coef28),2))
root28 = str(round(root28,2))

if float(coef28) < 0:

    formula28 = 'S'+'='+coef28+' '+'R'+'='+root28

else:

    formula28 = 'S'+'='+'+'+coef28+' '+'R'+'='+root28


ax28.annotate(formula28, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig29
file29 = pd.read_csv(path+'yangzhou.csv')

x29 = pd.DataFrame(file29['humidity'])
y29 = file29['o3']

trend29 = linear_model.LinearRegression()
trend29.fit(x29,y29)

y_pred29 = trend29.predict(x29)

ax29 = plt.subplot(gs[4,4])

ax29.set_xlim(0,100)
ax29.set_ylim(0,300)
x29_major_locator=MultipleLocator(25)
y29_major_locator=MultipleLocator(50)

ax29.scatter(x29,y29,color='red')
ax29.plot(x29,y_pred29,color='blue',linewidth=3)

#ax29.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax29.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax29.tick_params(labelsize=20)

ax29.annotate('yangzhou', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

#ax29.xaxis.set_major_formatter(plt.NullFormatter())
ax29.yaxis.set_major_formatter(plt.NullFormatter())
ax29.xaxis.set_major_locator(x29_major_locator)
ax29.yaxis.set_major_locator(y29_major_locator)

coef29 = trend29.coef_
root29 = math.sqrt(trend29.score(x29,y29))

coef29 = str(round(float(coef29),2))
root29 = str(round(root29,2))

if float(coef29) < 0:

    formula29 = 'S'+'='+coef29+' '+'R'+'='+root29

else:

    formula29 = 'S'+'='+'+'+coef29+' '+'R'+'='+root29


ax29.annotate(formula29, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig30
file30 = pd.read_csv(path+'zhenjiang.csv')

x30 = pd.DataFrame(file30['humidity'])
y30 = file30['o3']

trend30 = linear_model.LinearRegression()
trend30.fit(x30,y30)

y_pred30 = trend30.predict(x30)

ax30 = plt.subplot(gs[4,5])

ax30.set_xlim(0,100)
ax30.set_ylim(0,300)
x30_major_locator=MultipleLocator(25)
y30_major_locator=MultipleLocator(50)

ax30.scatter(x30,y30,color='red')
ax30.plot(x30,y_pred30,color='blue',linewidth=3)

#ax30.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax30.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax30.tick_params(labelsize=20)

ax30.annotate('zhenjiang', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

#ax30.xaxis.set_major_formatter(plt.NullFormatter())
ax30.yaxis.set_major_formatter(plt.NullFormatter())
ax30.xaxis.set_major_locator(x30_major_locator)
ax30.yaxis.set_major_locator(y30_major_locator)

coef30 = trend30.coef_
root30 = math.sqrt(trend30.score(x30,y30))

coef30 = str(round(float(coef30),2))
root30 = str(round(root30,2))

if float(coef30) < 0:

    formula30 = 'S'+'='+coef30+' '+'R'+'='+root30

else:

    formula30 = 'S'+'='+'+'+coef30+' '+'R'+'='+root30


ax30.annotate(formula30, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

###fig31
file31 = pd.read_csv(path+'zhoushan.csv')

x31 = pd.DataFrame(file31['humidity'])
y31 = file31['o3']

trend31 = linear_model.LinearRegression()
trend31.fit(x31,y31)

y_pred31 = trend31.predict(x31)

ax31 = plt.subplot(gs[5,0])

ax31.set_xlim(0,100)
ax31.set_ylim(0,300)
x31_major_locator=MultipleLocator(25)
y31_major_locator=MultipleLocator(50)

ax31.scatter(x31,y31,color='red')
ax31.plot(x31,y_pred31,color='blue',linewidth=3)

ax31.set_xlabel('RH (%)',fontsize=30, labelpad=0)
#ax31.set_ylabel('$\mathregular{O_{3}}$($\mu$g/m${^3}$)',fontsize=30, labelpad=0)
ax31.tick_params(labelsize=20)

ax31.annotate('zhoushan', xy=(0,1),xycoords='axes fraction',xytext=(5,-5),textcoords='offset points',fontsize=20,horizontalalignment='left',verticalalignment='top')

#ax31.xaxis.set_major_formatter(plt.NullFormatter())
ax31.xaxis.set_major_locator(x31_major_locator)
ax31.yaxis.set_major_locator(y31_major_locator)

coef31 = trend31.coef_
root31 = math.sqrt(trend31.score(x31,y31))

coef31 = str(round(float(coef31),2))
root31 = str(round(root31,2))

if float(coef31) < 0:

    formula31 = 'S'+'='+coef31+' '+'R'+'='+root31

else:

    formula31 = 'S'+'='+'+'+coef31+' '+'R'+'='+root31


ax31.annotate(formula31, xy=(0,1),xycoords='axes fraction',xytext=(5,23),textcoords='offset points',fontsize=18,horizontalalignment='left',verticalalignment='top')

################################################
plt.savefig('huadong.png')

