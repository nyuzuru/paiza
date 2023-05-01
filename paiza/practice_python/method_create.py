text = "pYthon"
print(text)
print(text.capitalize()) #capitalizeメソッド：先頭の文字を大文字にしてそれ以外は小文字
print(text.upper()) #upperメソッド：全て大文字になる

players = "勇者、戦士、魔法使い、忍者"
list = players.split("、") #splitメソッド：指定した文字列で分割してリストにする
print(list)
list.remove("忍者")
print(list)
list.append("中村")
print(list)
