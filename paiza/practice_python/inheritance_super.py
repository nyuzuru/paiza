# 親クラスのメソッドを継承先で呼び出す

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting): #Greetingクラスを継承（オーバーライド）
    def say_hello(self):
        super().say_hello() #Greetingクラスのsay_helloメソッドを呼び出す
        print("YEAH YEAH YEAH!")


player = Hello()
player.say_hello()