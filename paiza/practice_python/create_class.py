# クラスを作成する

class Player(): #クラス名の先頭は大文字にすること
    def walk(self): #walkメソッド
        print("勇者は歩いていた")
    
    def attack(self, enemy):
        print("勇者は" + enemy + "を攻撃した")

player1 = Player() #クラス名に（）をつけることでオブジェクトを作成できる
player1.walk() #player1が持っているwalkメソッドを呼び出している
player1.attack("スライム")