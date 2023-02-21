# 辞書をループで処理する

# 辞書のおさらい
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)

for rank in enemies:
    print(enemies[rank] + "が、あらわれた！")


# pythonのitemsメソッドを使う
for (rank, enemy) in enemies.items():
    print(rank + "の" + enemy + "が現れた")
# 最初の変数でキーを取り出して次の変数で値を取り出す。