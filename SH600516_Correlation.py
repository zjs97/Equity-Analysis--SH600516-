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
#日收益率取对数
stock_600516['stock_return']=np.log(stock_600516['close']/stock_600516['close'].shift(1))
index_hs300['hs300_return']=np.log(index_hs300['close']/index_hs300['close'].shift(1))
#计算两者的相关系数
correlation=stock_600516['stock_return'].corr(index_hs300['hs300_return'])
print(f'方大炭素与沪深300指数的日收益率相关系数为{correlation:.2}')






