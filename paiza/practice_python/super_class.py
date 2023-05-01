#  スーパークラスの継承

class Box:
    def __init__(self, item):
        self.item = item
        
    def open(self):
        print("宝箱を開いて、" + self.item + "を手に入れた")
        
class jewelryBox(Box): #クラスを継承するには（）の中にスーパークラスor親クラスを指定する
    def look(self):
        print("宝箱は輝いている")
        
box = Box("鋼鉄の剣")
box.open()

jewelryBox = jewelryBox("魔法の指輪")
jewelryBox.look()
jewelryBox.open()