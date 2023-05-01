class Enemy:
    def __init__(self, name):
        self.name = name
        
    def attack(self):
        print(self.name + "は勇者を攻撃した")
        
enemies = [] #enemiesリストを作成
enemies.append(Enemy("スライム")) #enemiesリストに"スライム"を追加
enemies.append(Enemy("ドラゴン"))
enemies.append(Enemy("モンスター"))

# for文でenemiesリストの中身を取得
for enemy in enemies:
    enemy.attack()