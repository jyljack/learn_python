# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 18:47
# @Author  : jiyl
# @File    : learn_dataframe.py

import pandas as pd
import numpy as np

# 读取CSV文件，创建DataFrame
# df = pd.read_csv("./data/dogNames2.csv")

# 创建DataFrame
df1 = pd.DataFrame(np.arange(12).reshape(3, 4))

# 根据字典创建DataFrame
dict1 = {"name": ["Jack", "Mike"], "age": [30, 20], "gender": ["male", "male"]}
df2 = pd.DataFrame(dict1)

# Series

print(type(df2["name"]))


