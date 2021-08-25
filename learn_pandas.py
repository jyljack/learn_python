# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 19:35
# @Author  : jiyl
# @File    : learn_pandas.py
import numpy as np
import pandas as pd

pd.set_option('expand_frame_repr', False)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
df = pd.read_csv("./data/austin_weather.csv", index_col="Date")

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
# 行index 列表查询
df2 = df.loc[['2017-07-27', '2017-07-28'], 'TempHighF']
# 列index 列表查询
df3 = df.loc['2017-07-27', ['TempHighF', 'TempLowF']]
# 行列都按照列表查询
df4 = df.loc[['2017-07-27', '2017-07-28'], ['TempHighF', 'TempLowF']]
# 行index 区间查询
df5 = df.loc['2017-07-27':'2017-09-20', ['TempHighF', 'TempLowF']]
# 条件查询
df6 = df.loc[(df['TempLowF'] < 50) & (df['TempHighF'] > 79), :]
# lambda
df7 = df.loc[lambda d: (d['TempLowF'] < 50) & (d['TempHighF'] > 79), :]

# 新增列
df.loc[:, "wencha"] = df["TempHighF"] - df['TempLowF']


# 新增列 apply
def get_type(x):
    if x['TempHighF'] > 60:
        return "高温"
    if x['TempLowF'] > 50:
        return "低温"
    return "常温"


df.loc[:, 'Type'] = df.apply(get_type, axis=1)

# 新增DataFrame assign
df8 = df.assign(
    TempHighC=lambda x: (x['TempHighF'] - 32) * 5 / 9,
    TempLowC=lambda x: (x['TempLowF'] - 32) * 5 / 9
)

_df = pd.read_csv("./data/austin_weather.csv")
print(type(_df['Date'][0]))
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
_df['Date'] = pd.to_datetime(_df['Date'], format='%Y-%m-%d')
print(type(_df['Date'][0]))

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html
# DataFrame.resample(rule, axis=0, closed=None, label=None, convention='start', kind=None, loffset=None,
# base=None, on=None, level=None, origin='start_day', offset=None)
df9 = _df.resample(rule='5D', on='Date', label='left', closed='left').agg(
    {'TempHighF': 'max',
     'TempAvgF': 'mean',
     'TempLowF': 'min',
     })
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)[source]
df9.dropna(subset=['TempHighF'], inplace=True)
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
# DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
df9.reset_index(inplace=True)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html
# DataFrame.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None)
df10 = pd.DataFrame(np.random.randn(7, 4), index=pd.date_range('1/1/2020', periods=7), columns=['A', 'B', 'C', 'D'])
print(df10)
df10_mean = df10.rolling(window=3, min_periods=1).mean()
print(df10_mean)
df10_std = df10.rolling(window=3, min_periods=1).std(ddof=0)
print(df10_std)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html
# DataFrame.sum(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, **kwargs)[source]
df10['sum'] = df10.sum(axis=1, skipna=True)
print(df10)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shift.html
# DataFrame.shift(periods=1, freq=None, axis=0, fill_value=None)
df10_shift1 = df10.shift(axis=0)
df10_shift2 = df10.shift(axis=1)
print(df10_shift1)
print(df10_shift2)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html
# DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)[source]

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_hdf.html
# DataFrame.to_hdf(path_or_buf, key, mode='a', complevel=None, complib=None, append=False, format=None, index=True,
# min_itemsize=None, nan_rep=None, dropna=None, data_columns=None, errors='strict', encoding='UTF-8')
