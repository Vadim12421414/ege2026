print('A B C D')
for a in range(2):
    for b in(0, 1):
        for c in [0, 1]:
            for d in 0, 1:
                f=not(a<= b) or (c<=b) or not a
                if not f:
                    print(a, b, c, d)