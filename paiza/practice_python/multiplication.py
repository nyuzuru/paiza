# 掛け算の九九を表示

def multiplication(x, y):
    return x * y

for step in range(1,10):
    for num in range(1,10):
        print(multiplication(step, num), end="")
        if num < 9:
            print("," , end="")
    print("")