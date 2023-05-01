# 半角スペースでの出力
'''
文字列の結合を使う。
'''

# 解答１
n = int(input())

ans = "paiza"

for i in range(n-1):
    ans += " paiza" #半角スペースを入れることで出力した時に半角区切りになる

print(ans)


# 解答２
n = int(input())

p = ["paiza"] * n

print(" ".join(p))
# pの要素を” ”区切り（今回は半角スペース）で繋げた文字列を返す