# 数字の文字列操作（時刻２）
'''
与えられた時刻の３０分後が繰り上がるかどうかを求められるかが鍵
'''

s = input()
h = int(s[:2])
m = int(s[3:])

if m+30 >= 60:
    h = str(h+1)
    m = str(m+30-60)
else:
    h = str(h)
    m = str(m+30)

if len(h) == 1:
    h = "0"+h
if len(m) ==1:
    m = "0"+m

print(h+":"+m)