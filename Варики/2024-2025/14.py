from string import printable as alph

for x in alph[:19]:
    num1 = int(f'98897{x}21', 19)
    num2 = int(f'2{x}923', 19)  # всё верно, цифра 3 есть
    num = num1 + num2
    if num % 18 == 0:
        print(num // 18)