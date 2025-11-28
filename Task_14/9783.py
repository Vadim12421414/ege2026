from string import printable as alph
for x in (alph[:22]):
    mun1=int(f'18{x}89957', 22)
    mun2=int(f'80{x}33', 22)
    mun3=int(f'521{x}6', 22)
    num= mun1 + mun2 + mun3
    if num%21==0:
        print(x, num//21)
