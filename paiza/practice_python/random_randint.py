# randomモジュール使い方
import random

def attack(enemy):
    print("勇者は"+enemy+"を攻撃した")
    hit = random.randint(1,10)
    if hit < 6:
        print(enemy+"に"+str(hit)+"を攻撃した")
    else:
        print("クリティカルヒット"+enemy+"に100のダメージ")

enemies = ["スライム","モンスター","ドラゴン"]
for enemy in enemies:
    attack(enemy)