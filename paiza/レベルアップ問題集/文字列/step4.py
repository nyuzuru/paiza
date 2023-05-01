# 数字の文字列操作
'''
while文で文字列を指定の長さになるまで０を追加させればよい
'''

n = input()

while len(n) < 3:
    n = "0" + n

print(n)