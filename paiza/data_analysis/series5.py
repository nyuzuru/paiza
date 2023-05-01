# index属性
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s.index)  # インデックスの取得
s.index = ["d", "e", "f"]  # インデックスの書き換え


# name属性
import pandas as pd

s = pd.Series([3, 1, 2], name="nums")
print(s.name)  # 名前の取得
new_s = s.rename("values")  # 名前の付け替え
s.rename("values", inplace=True)  # sそのものの名前の変更
s.index.name = "chars"  # インデックスのname属性を指定

# dtype属性
import pandas as pd

s = pd.Series([3, 1, 2], name="nums")
print(s.dtype)  # dtypeの取得

s = pd.Series([3, 1, 2], name="nums", dtype="float64")  # dtypeを指定