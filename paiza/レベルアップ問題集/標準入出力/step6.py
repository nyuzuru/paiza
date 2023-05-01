# 改行区切りでの出力
'''
splitをうまく使えるかどうかがポイント
'''

n = int(input())

# input().split()は入力された数値をリストにする。
a = input().split()

for i in range(n):
    print(a[i])