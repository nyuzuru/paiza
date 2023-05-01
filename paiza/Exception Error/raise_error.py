# raise：意図的に例外処理を起こす

print(1)
try:
    print(2)
    #raise()の引数を指定しなければ空行として出力される
    raise Exception("意図的な例外") 
    print(3)
except Exception as e:
    print("予期せぬエラーが発生しました")
    print(e)
finally:
    print(4)
