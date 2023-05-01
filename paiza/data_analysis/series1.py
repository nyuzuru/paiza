# pandasは標準ライブラリではないため、本来はインストールする必要がある。

import pandas as pd

# Seriesの作成
s = pd.Series({"a":3, "b":1, "c":2})
# print(s)

ind =["a", "b", "c"]
s2 = pd.Series(1, index=ind)
# print(s2)

s3 = pd.Series([3, 1, 2], index=["a", "a", "c"])
print(s3)
