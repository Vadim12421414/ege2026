def f(start, end):
    if start>=end: return start==end# не пон, почему так
    if start > end: return 0
    return f(start + 2, end) + f(start + 5, end) + f(start ** 2, end)
print(f(4, 36)-1)#так как у нас только одна команда не подходит  из за условия

