# ソート

# インデックスによるソート
import pandas as pd


s = pd.Series({"b": 3, "c": 1, "a": 2})

print(s.sort_index())  # 昇順
print(s.sort_index(ascending=False))  # 降順


# 値によるソート
import pandas as pd


s = pd.Series({"b": 3, "c": 1, "a": 2})

print(s.sort_values())  # 昇順
print(s.sort_values(ascending=False))  # 降順