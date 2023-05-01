# 入力の配列による保持
'''
今回は入力した値を配列として保持する必要がある。そこがポイント
'''

n = int(input())

A = [0] * n

for i in range(n):
    a = int(input())
    A[i] = a

print(max(A))