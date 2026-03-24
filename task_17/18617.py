with open() as file:
    data = [int(i) for i in file]
maxx = max(data)
minn = min(data)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 3 == maxx % 3
    u2 = num2 % 3 == maxx % 3
    u3 = num1 % 7 == minn % 7
    u4 = num2 % 7 == minn % 7
    if u1 + u2 >= 1 and u3 + u4 >= 1:
        ans.append(sum(num1, num2))
print(len(ans), max(ans))

