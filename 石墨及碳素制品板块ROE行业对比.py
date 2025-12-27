# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 15:16:36 2025

@author: zjs97
"""
#导入库
import akshare as ak
import matplotlib.pyplot as plt
import matplotlib
#导入数据
stocks = ak.stock_zh_dupont_comparison_em(symbol="SH600516")
#筛选数据并确认中文字体
stock=stocks.iloc[2:]
matplotlib.rcParams['font.family']='SimHei'
#进行数据可视化
fig, ax = plt.subplots()
ax.bar(stock['简称'],stock['ROE-3年平均'])
ax.set_ylabel("ROE(%)",fontsize=16)
ax.set_xlabel('企业名称',fontsize=16)
ax.set_title('石墨及碳素制品板块ROE行业对比',fontsize=16)
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()