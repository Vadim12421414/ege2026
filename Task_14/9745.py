from string import printable as alph
for x in (alph[:19]):
    mun1=int(f'98{x}79641', 19)
    mun2=int(f'36{x}14', 19)
    mun3=int(f'73{x}4', 19)
    num= mun1 + mun2 + mun3
    if num%18==0:
        print(x, num//18)
