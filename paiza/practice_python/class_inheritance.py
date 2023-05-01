# 継承
class Player:
    def __init__(self, name):
        self.name = name
    
    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した")
        
print("== パーティーでスライムと戦う ==")

hero = Player("勇者")
warrior = Player("戦士")

party = [hero, warrior]
for member in party:
    member.attack("スライム")