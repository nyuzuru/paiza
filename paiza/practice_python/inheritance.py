# 継承の練習問題
class Player:
    def __init__(self, name):
        self.name = name
        
    def attack(self, enemy):
        print(self.name + "" + enemy + "を攻撃した")
        
class Warrior(Player): #Playerクラスをオーバーライド
    def attack(self, enemy):
        print(self.name + "" + enemy + "を猛攻撃した")
        
team = [] #teamの空のリスト作成
team.append(Player("勇者"))
team.append(Player("魔法使い"))
team.append(Warrior("戦士"))

for person in team:
    person.attack("スライム")