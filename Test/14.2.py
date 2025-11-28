from string import printable as  alph
for x in alph[:25]:
    mun1=int(f'a4{x}7f2', 25)
    mun2=int(f'n{x}g5{x}h', 25)
    mun3=int(f'74{x}m26',25)
    num= mun1 + mun2 + mun3
    if num%24==0:
        print(x, num//24)


