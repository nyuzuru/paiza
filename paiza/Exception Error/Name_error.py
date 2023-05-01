# 例外処理機能：NameError

print(1)
try:
    number = 1
    answer = 100 / number
    print(answer2)
except NameError as e:
    print("未定義変数です")
    print(e)
finally:
    print(2)
