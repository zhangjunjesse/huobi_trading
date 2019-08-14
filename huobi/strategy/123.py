#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
123法则。
1：突破趋势线
2：上升不破新高，下降不破新低
3：上升突破M低，下降突破W头

"""
from HuobiServices import *

def get_close_line(period="5min", size=150):
    data = get_kline("btcusdt", period, size=size)
    closes = []
    for d in data['data']:
        closes.append([d['id'],d['close']])
    closes.reverse()
    return closes

#获取压力线的点
def get_close_high_line(period="5min", size=150):
    closes = get_close_line()
    highs = []
    for i in range(len(closes)):
        if i >= 1 and i <= len(closes) - 2  :
            if closes[i] > closes[i-1] and closes[i] > closes[i+1] :
                highs.append([i+1,closes[i]])
    return highs

#获取支撑线的点
def get_close_low_line(period="5min", size=150):
    closes = get_close_line()
    lows = []
    for i in range(len(closes)):
        if i >= 1 and i <= len(closes) - 2  :
            if closes[i] < closes[i-1] and closes[i] < closes[i+1] :
                lows.append([i+1,closes[i]])
    return lows


    
closes = get_close_line(period="1min",size=200)



        

import matplotlib.pyplot as plt#约定俗成的写法plt
#首先定义两个函数（正弦&余弦）
import numpy as np

x = np.linspace(closes[0][0], closes[-1][0], len(closes))
close_line = []
for cell in closes:
    close_line.append(cell[1])
y1 = close_line      # 曲线 y1
plt.figure()    # 定义一个图像窗口
plt.plot(x, y1) # 绘制曲线 y1

# highs = []
# lows = []
# 
# for i in range(len(closes)):
#     if i >= 1 and i <= len(closes) - 2  :
#         if closes[i] > closes[i-1] and closes[i] > closes[i+1] :
#             plt.scatter([i+1], [closes[i]], s=10, color="blue")      # s 为点的 size
#             highs.append([i+1,closes[i]])
#         if closes[i] < closes[i-1] and closes[i] < closes[i+1] :
#             plt.scatter([i+1], [closes[i]], s=10, color="red")      # s 为点的 size
#             lows.append([i+1,closes[i]])

plt.show()

# ax = 136 
# ay = 10614
# bx = 139
# by = 10583
# # cx = 142
# # cy = 10593
# cx = 133
# cy = 10593
# kac=(ax-cx)*(cy-by)
# kbc=(cx-bx)*(ay-cy)   
# print(kac - kbc)