# ラベルによる値の参照
import pandas as od

s = pd,Series({"a":3, "b":1, "c":2})
print(s["a"])
# 3が出力される


# ラベルによるスライシング
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s["b":"c"])
# b 1 と c 2 が出力される


# 整数インデックスによるスライシング
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s[1:2])
# b 1 が出力される


# ラベルのリストによる参照
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
ind = ["a", "c"]
print(s[ind])
# ラベル"a"と"b"に該当するものが表示される