# クラスからオブジェクトを作成する

class Greeting:
    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print("hello " + self.name)
        
call_name = Greeting("nakamura")
call_name.say_hello()