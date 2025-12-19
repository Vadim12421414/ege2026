print('X Y Z W')
for y in range(2):
    for x in(0, 1):
        for z in [0, 1]:
            for w in 0, 1:
                f = ((z<=x)<=y) or not w
                if not f:
                    print(x, y, z, w)