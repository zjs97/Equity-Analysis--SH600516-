# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 09:55:04 2025

@author: zjs97
"""
#导入库
import akshare as ak
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#从Akshare导入数据
stock_600516 = ak.stock_zh_a_hist(symbol="600516", period="daily", start_date="20201231", end_date='20251227', adjust="qfq")
#选择绘图的中文字体
matplotlib.rcParams['font.family']='SimHei'
#将时间格式转变为pandas格式
stock_600516['日期']=pd.to_datetime(stock_600516['日期'])
#将绘图区域一分为二
fig,(ax1,ax2)=plt.subplots(2,1)
#设置图1的横纵坐标变量并进行图例优化
ax1.plot(stock_600516['日期'],stock_600516['收盘'])
ax1.grid(True,which='major',axis='y',linestyle="--",alpha=0.7)
#进行图片标题，Y轴单位，刻度的设置
ax1.set_title('2025年方大炭素股票走势',fontsize=16)
ax1.set_ylabel("收盘价（元）",fontsize=16)
ax1.tick_params(labelsize=16)
#设置图2柱状图颜色。并确定横纵坐标及字体大小
colors=['red' if row['收盘']>=row['开盘'] else 'green' for index,row in stock_600516.iterrows()]
ax2.bar(stock_600516['日期'],stock_600516['成交量']/10000,color=colors)
ax2.set_ylabel("成交量（万手）",fontsize=16)
ax2.set_xlabel('日期',fontsize=16)
#数据可视化
fig.autofmt_xdate()
plt.show()

#计算该股票近5年的总收益率
total_return=list(stock_600516['收盘'])[-1]/list(stock_600516['收盘'])[0]-1
#计算该股票的年化收益率
annual_return=pow(1+total_return,250/len(stock_600516))-1
print(f"方大炭素近5年的年化收益率是{total_return*100:.4}%，年化收益是{annual_return*100:.4}%。")
#计算该股票近5年的最大回撤率
stock_600516['max_close']=stock_600516['收盘'].cummax()
stock_600516['drawdown']=(stock_600516['max_close']-stock_600516['收盘'])/stock_600516['max_close']
max_drawdown=stock_600516['drawdown'].max()
print(f"方大炭素近5年的最大回撤率:{round(max_drawdown*100,2)}%")
#计算该股票的波动率及夏普比例
day_returns=stock_600516['收盘']/stock_600516['收盘'].shift(1)-1
volatility=day_returns.std()*np.sqrt(250)
Sharpe_Ratio=(annual_return-0.19)/volatility
print(f"方大炭素最近5年的波动率是:{volatility*100:.4}%，夏普比率是：{Sharpe_Ratio:.2}。")

