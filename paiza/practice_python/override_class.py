# オーバーライド：スーパークラスが持つメソッドをサブクラスで書き換えて再定義すること
class Box:
    def __init__(self, item):
        self.item = item
    
    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた")
    
class MagicBox(Box): #（）の中に親クラスを書くことで継承している
    def look(self):
        print("宝箱は怪しく輝いている")
        
    def open(self): #親クラスが持つメソッドを再定義している。これがオーバーライド
        
        print("宝箱を開いた。" + self.item + "が襲ってきた")
        

box = Box("魔法の剣")
box.open()

magixbox = MagicBox("モノマネモンスター")
magixbox.look()
magixbox.open()