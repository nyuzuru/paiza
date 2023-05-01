# 更新、追加、削除

import pandas as pd


s = pd.Series({"a": 3, "b": 1, "c": 2})

s["a"] = 813
s["d"] = 100
del s["d"]  # del文による削除
# print(s.pop("a"))  # 値の削除と削除された値の取得
print(s.drop("a"))  # 要素を削除した新しいSeriesを返す
print()

print(s)