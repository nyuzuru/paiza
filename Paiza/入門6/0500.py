# enumerate:ループでインデックスを使いたい時に使う

team = ["勇者", "戦士", "魔法使い"]

for (i, person) in enumerate(team):
    print(str(i+1) + "番目の" + person + "が、スライムと戦った")


# forで新しい配列を作る
numbers = [3, 1, 4, 1, 5]
results = []
for item in numbers:
    results.append(item * 10)

print(results)