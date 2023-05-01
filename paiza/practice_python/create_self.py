# 変数をクラスで管理。selfの理解。コンストラクタの理解

class Player():
    # コンストラクタ：クラスからオブジェクトを作成する際に最初に呼ばれるメソッド
    def __init__(self, job):
        # self：インスタンス変数を使う際に必要になる引数
        self.job = job #self.〇〇のことをインスタンス変数と呼ぶ。オブジェクトが持つ変数のこと
        
    def walk(self):
        print(self.job + "は高野を歩いていた")
        
player1 = Player("戦士")
player1.walk()

player2 = Player("魔法使い")
player2.walk()

player1.walk()

        