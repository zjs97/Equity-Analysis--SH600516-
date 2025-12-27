# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 15:32:27 2025

@author: zjs97
"""
#导入库
import akshare as ak
import pandas as pd
import numpy as np

#导入股票数据
stock_600516 = ak.stock_zh_index_daily(symbol="sh600516")
#转换日期格式并确定研究时间
stock_600516['date']=pd.to_datetime(stock_600516['date'])
stock_600516=stock_600516[(stock_600516['date']>='2020-12-31')&(stock_600516['date']<='2025-12-27')]
stock_600516.set_index('date',inplace=True)
#导入指数数据
index_hs300 = ak.stock_zh_index_daily(symbol="sh000300")
#转换日期格式并确定研究时间
index_hs300['date']=pd.to_datetime(index_hs300['date'])
index_hs300=index_hs300[(index_hs300['date']>='2020-12-31')&(index_hs300['date']<='2025-12-27')]
index_hs300.set_index('date',inplace=True)
#将两者收盘合并入一个Dataframe中
combined=pd.DataFrame({'stock_close':stock_600516['close'],'hs300_close':index_hs300['close']})
#将两者的日收益率进行指数化
combined['stock_return']=np.log(combined['stock_close']/combined['stock_close'].shift(1))
combined['hs300_return']=np.log(combined['hs300_close']/combined['hs300_close'].shift(1))
#计算两者的相关系数
correlation=combined['stock_return'].corr(combined['hs300_return'])
print(f'方大炭素与沪深300指数的日收益率相关系数为{correlation:4f}')



