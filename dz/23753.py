from string import printable as alph
for x in alph[:29]:
    r1 = int(f'923{x}874', 29)
    r2 = int(f'524{x}6152', 29)
    r = r1+r2
    if r%28==0:
        print(r//28, x)