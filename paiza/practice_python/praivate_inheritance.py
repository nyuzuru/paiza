# プライベートメソッドをクラス外で呼び出
class Greeting:
    def __ini__(self):
        self.msg = "hello"
        self.target = "paiza"
        
    def say_hello(self):
        print(self.msg + " " + self.target)
        
    def __say_yeah(self): #メソッド名の先頭に__をつけるとプライベートメソッドになる。基本的にクラス外では呼び出せない
        print("YEAH")
    
player = Greeting()
player.say_hello()
player._Greeting__say_yeah() #呼び出す時は「_クラス名__メソッド名」と記載する
