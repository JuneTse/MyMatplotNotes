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


x = [100,500,1000,1500,2000,2500,3000]
y = [76.35,77.6,78.2,78.5, 78.77,78.89,79]


plt.figure(figsize=(8,6)) 
plt.xlim(0,3100)
#plt.xticks(x)


plt.xticks(x,fontsize=fontsize)
plt.yticks(fontsize=fontsize)

plt.plot(x,y,linestyle='solid', marker='^',c='red',markersize=8)

#plt.xlabel("Top K candidates")
#plt.ylabel('Accuracy(%)')

plt.xlabel("Top K candidates",fontsize=fontsize)
plt.ylabel('Accuracy(%)',fontsize=fontsize)

plt.legend(['SimpleQuestions'],loc='lower right',fontsize=fontsize)
figname='fig4.eps'  
plt.savefig(figname)  
plt.show()


############## NLPCC2016 #################

x = [100,500,1000,1500,2000,2500,3000]
y = [81.95,83,83.19,83.21, 83.3,83.34,83.45]


plt.figure(figsize=(8,6)) 
plt.xlim(0,3100)
#plt.xticks(x)


plt.xticks(x,fontsize=fontsize)
plt.yticks(fontsize=fontsize)

plt.plot(x,y,linestyle='solid', marker='o',c='green',markersize=8)

#plt.xlabel("Top K candidates")
#plt.ylabel('Average $F_1$(%)')

plt.xlabel("Top K candidates",fontsize=fontsize)
plt.ylabel('Average $F_1$(%)',fontsize=fontsize)

plt.legend(['NLPCC 2016 testing data'],loc='lower right',fontsize=fontsize)
figname='fig5.eps'  
plt.savefig(figname)  
plt.show()