# 変数の先頭に+をつけると可変超引数となりリストになる。

def introduce(greeting, *names): #namesが可変超引数になっている
    for  name in names:
        print("私は"+ name + "です" + greeting)

introduce("こんにちは","勇者","村人","兵士")



# 可変超引数は辞書としても使える
def intro(**people):
    for  name, greeting, in people.items():
        print("私は"+ name + "です" + greeting)
    print(people)

intro(hero="初めまして", villager="こんにちは", soldier="よろしくお願いします")
