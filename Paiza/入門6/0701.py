# ドット絵の表示
for line in letter_A:
    for dot in line:
        if dot ==1:
            print("@", end="")
        else:
            print(" ", end="")
    print("")
