import traceback, sys
#スタックトレース：プログラムの実行過程を表示するモジュール

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
    # print(traceback.format_exc())
    # format_exc()メソッド：例外情報を文字列として取得できる
    sys.stderr.write(traceback.format_exc())
    # sysはプログラマー向けにエラー内容を表示させてくれる
finally:
    print(2)