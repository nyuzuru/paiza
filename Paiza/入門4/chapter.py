# append関数：リストの末尾に要素を追加
team = ["勇者", "魔法使い"]
team.append("戦士") #teamのリストに"戦士"を追加
print(team)


# リストの要素を削除
new_team = ["勇者", "魔法使い", "戦士"]
new_team.pop(2) #リストの3番目（戦士）を削除する
print(new_team)


# rstrip関数：文字列の末尾の改行コードを取り除く。
line = input().rstrip()


# split関数：与えられたデータを指定の記号で分割し、リストとして戻す
line = "勇者,戦士,魔法使い"
print(line.split(","))


# readkines関数：読み込んだデータを一行ごとに処理(複数行入力される場合に使う)
import sys
for line in sys.stdin.readlines():
	msg = line.rstrip()
	print(msg + "が現れた")


# リストを作ったランダムくじ
import random
line = input().rstrip().split(",")
for enemy in line:
	print(enemy + "が現れた！")
# ランダムな数を作る範囲を調べる
num = len(line)
print("敵は"+str(num)+"匹")
# ランダムな数を生成
attack = random.randrange(num)
print(line[attack] + "会心の一撃" + line[attack] + "を倒した")




# じゃんけんプログラム
import random
# 標準入力から1行取得
line = input().rstrip()
# カンマで分割して、リストに代入
janken =line.split(",")
# リストの要素数を変数に代入
num = len(janken)
# リストの中身を出力
print(janken)
# ランダムに選んだリストの要素を出力
print(janken[random.randrange(num)])




# おみくじプログラム
import random
line = input().rstrip()
# カンマで分割して、リストに代入
omikuji = line.split(",")
# リストの要素数を変数に代入
num = len(omikuji)
# リストの中身を出力
print(omikuji)
# ランダムに選んだリストの要素を出力
print(omikuji[random.randrange(num)])
