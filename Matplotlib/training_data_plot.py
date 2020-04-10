import matplotlib.pyplot as plt
import numpy as np



# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib  
matplotlib.use('qt4agg')  
#指定默认字体  
#matplotlib.rcParams['font.sans-serif'] = ['SimHei']   
#matplotlib.rcParams['font.family']='sans-serif'  
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus'] = False  

fontsize=18


x = [0.5,0.6,0.7,0.8,0.9,1.0]
y = [76.45,76.8,77.05,77.35, 77.9,79]
y2=[73.9, 74.2, 74.4, 74.9, 75.35, 76.5]


plt.figure(figsize=(8,6)) 
#plt.xlim(0.4,1.1)
#plt.xticks(x)


plt.xticks(x,fontsize=fontsize)
plt.yticks(fontsize=fontsize)

plt.plot(x,y,linestyle='solid', marker='^',c='red',markersize=8)
plt.plot(x,y2,linestyle='solid', marker='o',c='green',markersize=8)

#plt.xlabel("Top K candidates")
#plt.ylabel('Accuracy(%)')

plt.xlabel("The ratio of data used to train for SimpleQuestions",fontsize=fontsize)
plt.ylabel('Accuracy(%)',fontsize=fontsize)

plt.legend(['MLSM','DSM'],loc='lower right',fontsize=fontsize)

figname='fig6.eps'  
plt.savefig(figname)  
plt.show()


############## NLPCC2016 #################

x = [0.5,0.6,0.7,0.8,0.9,1.0]
y = [81.8,81.98,82.25,82.55, 82.79,83.45]
y2=[80.48, 81, 81.2, 81.25, 81.45,81.7]


plt.figure(figsize=(8,6)) 
#plt.xlim(0.4,1.1)
#plt.xticks(x)


plt.xticks(x,fontsize=fontsize)
plt.yticks(fontsize=fontsize)

plt.plot(x,y,linestyle='solid', marker='^',c='red',markersize=8)
plt.plot(x,y2,linestyle='solid', marker='o',c='green',markersize=8)


#plt.xlabel("Top K candidates")
#plt.ylabel('Average $F_1$(%)')

plt.xlabel("The ratio of data used to train for NLPCC 2016",fontsize=fontsize)
plt.ylabel('Average $F_1$(%)',fontsize=fontsize)

plt.legend(['MLSM','DSM'],loc='lower right',fontsize=fontsize)
figname='fig7.eps'  
plt.savefig(figname)  
plt.show()