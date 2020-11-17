#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 10:09
# @Author  : fuGuowen
# @Site    : 
# @File    : test01.py
# @Software: PyCharm

# 上证指数预测，使用时间序列ARMA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA
import warnings
from itertools import product
from datetime import datetime
warnings.filterwarnings('ignore')
# ARMA 模型对沪市指数未来 10 个月（截止到 2019 年 12 月 31 日）的变化进行预测（将数据转化为按月统计即可）
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# 数据加载
df = pd.read_csv('./shanghai_1990-12-19_to_2019-2-28.csv')
# 将时间作为df的索引
df.Timestamp = pd.to_datetime(df.Timestamp)
df.index = df.Timestamp
# 数据探索
print(df.head())
# 按月对数据进行下采样
df_month = df.resample('M').mean()
print(df_month.head())

# 设置参数范围
ps = range(0, 3)
qs = range(0, 3)
parameters = product(ps, qs)
parameters_list = list(parameters)
# 寻找最优ARMA模型参数，即best_aic最小
results = []
best_aic = float("inf") # 正无穷
for param in parameters_list:
    try:
        model = ARMA(df_month.Price,order=(param[0], param[1])).fit()
    except ValueError:
        print('参数错误:', param)
        continue
    aic = model.aic
    if aic < best_aic:
        best_model = model
        best_aic = aic
        best_param = param
    results.append([param, model.aic])
# 输出最优模型
result_table = pd.DataFrame(results)
result_table.columns = ['parameters', 'aic']
print('最优模型: ', best_model.summary())

# 比特币预测
df_month2 = df_month[['Price']]
# 又增加了11列做预测
date_list = [datetime(2019, 3, 31), datetime(2018, 4, 30), datetime(2019, 5, 31), datetime(2019, 6, 30), datetime(2019, 7, 31),
             datetime(2019, 8, 31), datetime(2019, 9, 30), datetime(2019, 10, 31),datetime(2019, 11, 30),datetime(2019, 12, 31),
             datetime(2020,1, 31),datetime(2020,2, 28),datetime(2020,3, 31),datetime(2020,4, 30),datetime(2020,5, 31),datetime(2020,6, 30),
             datetime(2020,7, 31),datetime(2020,8, 31),datetime(2020,9, 30),datetime(2020,10, 31),datetime(2020,11, 30),datetime(2020,12, 31)]
future = pd.DataFrame(index=date_list, columns= df_month.columns)
df_month2 = pd.concat([df_month2, future])
df_month2['forecast'] = best_model.predict(start=0, end=361)
# 打印预测的最后30条数据结果
print(df_month2[-30:])
# 比特币预测结果显示
plt.figure(figsize=(20,7))
df_month2.Price.plot(label='实际指数')
df_month2.forecast.plot(color='r', ls='--', label='预测指数')
plt.legend()
plt.title('上证指数（月）')
plt.xlabel('时间')
plt.ylabel('元')
plt.show()