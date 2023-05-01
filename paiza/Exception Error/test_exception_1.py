# 呼び出し元へ例外を伝える位

import sys

def calc():
    return 100 / 0
try:
    print(calc())
except ZeroDivisionError as e:
        sys.stderr.write("0で割り算はできません")