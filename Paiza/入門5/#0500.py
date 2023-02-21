# リストの整列
# リストの整列
weapons = ["イージスソード", "ウィンドスピア", "アースブレイカー", "イナズマハンマー"]
print(weapons)

print(sorted(weapons))
print(sorted(weapons, reverse=True))
# 辞書で並び順を逆にする場合はreverseパラメータを使用する。

weapons2 = ["4.イージスソード", "1.ウィンドスピア", "3.アースブレイカー", "2.イナズマハンマー"]
print(sorted(weapons2))

weapons3 = ["バーニングソード", "風神スピア", "大地ブレイカー", "稲妻ハンマー"]
print(sorted(weapons3))