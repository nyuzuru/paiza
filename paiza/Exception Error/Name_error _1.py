import sys

enemies = ["スライム", "ドラゴン", "魔王"]

try:
    number1 = 0
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[number2] + "と戦った")
except NameError as e:
    sys.stderr.write("未定義の変数を呼び出しています")
except NameError as e:
    sys.stderr.write("未定義の変数を呼び出しています")
finally:
    print("勇者は勝利した")
