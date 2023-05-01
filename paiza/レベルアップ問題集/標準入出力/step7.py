# 標準入出力ラスト

N = int(input())

for i in range(N):
    # 社員の名前と前年度の年齢の組をリストとして保存
    s_a = input().split() 
    s = s_a[0] # 社員の名前は最初の要素
    a = int(s_a[1]) # 社員の年齢は２番目の要素
    print(s, a+1)