# 入力された分だけ画像を挿入

# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# ここから下を記述しよう
num = int(input())
# print(num)
while num > 0:
    item = input()
    print("<img src ='" + items_imges[item] + "'>")
    num = num -1