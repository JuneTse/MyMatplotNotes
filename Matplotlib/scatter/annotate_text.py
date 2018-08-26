#coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

'''
在二维平面上画散点图，并给每个点标注文本标签
1. scatter: 画散点图
2. annotate: 添加文本标签
    参数： 
    s: 标签文本
    xy: 点的位置
    xytext: 文本的位置
    textcoords: 文本的坐标，offset points表示xytext中是相对位置，默认为绝对位置
    ha: 水平对齐方式
    va: 垂直对齐方式
'''

data=np.random.rand(50,2)
labels=list(range(50))

#可视化
fig=plt.figure(figsize=(8,8))
#遍历每个点使用scatter画点，使用annotate画点的标签
for (x,y),label in zip(data,labels):
    plt.scatter(x,y,color='red',lw=2,label=labels)
    plt.annotate(s=label,
                 xy=(x,y),
                 xytext=(5,2), #文本的位置，与textcoords配合使用，offset points表示相对点坐标的偏移量，否则是绝对位置
                 textcoords='offset points', #文本的坐标，可能与点的坐标不同
                 ha='right',
                 va='bottom')
