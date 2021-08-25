# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 18:47
# @Author  : jiyl
# @File    : learn_series.py

import pandas as pd
import numpy as np

# 创建Series
s1 = pd.Series([1, 2, 31, np.nan, 12, 4])

# 创建Series，并指定Index
s2 = pd.Series([1, 2, 31, 12, 4], index=list("abcde"))

# 通过字典创建Series，Key 作为Index
temp_dict = {"name": "Jack", "age": 30, "gender": "male"}
s3 = pd.Series(temp_dict)


# Series 切片
