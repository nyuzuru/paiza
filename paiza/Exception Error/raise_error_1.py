import sys

print("Hello World")

try:
    raise ZeroDivisionError("強制エラー")
except NameError as e:
    sys.stderr.write("未定義の変数を呼び出しています")
except ZeroDivisionError as e:
    sys.stderr.write("0では割り算できません") #sys.stderr.write()は標準エラーに文字列を出力する


finally:
    print("Hello Python3")