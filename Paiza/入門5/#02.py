# リストのおさらい
enemyArray = ["スライム","モンスター","ドラゴン"]
print(enemyArray)
print(enemyArray[0])


# 辞書の具体例
enemyDictionary = {"ザコ":"スライム","中ボス":"ドラゴン","ラスボス":"魔王"}
print(enemyDictionary)
print(enemyDictionary["ザコ"])

level = "ラスボス"
print(enemyDictionary[level])

# del関数 リストからキーの値を削除できる
del enemies["ザコ"]
print(enemies)
print(len(enemies))