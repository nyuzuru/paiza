# 継承_2
class Player:
    def __init__(self, name):
        self.name = name
    
    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した")

class Wizard(Player):
    def attack(self, enemy):
        print(self.name + "は、" + enemy + "に炎を放った")
        
        
print("== パーティーでスライムと戦う ==")

hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard("魔法使い")

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")