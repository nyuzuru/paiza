# フィルタリング
'''
フィルタリングはデータ分析でよく使う
'''

import pandas as pd


s = pd.Series({"a": 3, "b": 1, "c": 2})
p = pd.Series([True, True, False])
q = pd.Series([True, False, True])

print(p&q)
print(p|q)
print(~q)


# 複数条件によるフィルタリング
t = pd.Series([3, 5, 15])
print(t[(t % 3 == 0) & (t % 5 == 0)])