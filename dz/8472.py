def convert(num, sys):
    res=''
    while num:
        res+=str(num % sys)
        num//=sys
    return res[::-1]
for i in range(1, 100):
    num_1=7*100**6 + 10*100**5 + i*100**4 + 0*100**3 + 1*100**2 + 2*100**1 + 3*100**0
    num_2=1*100**5 + 11*100**4 + 10*100**3 + 6*100**2 + 4*100**1 + i*100**0
    num_3=i*100**6 + 9*100**5 + 8*100**4 + 0*100**3 + 1*100**2 + 2*100**1 + 12*100**0
    num_all=num_1 - num_2+num_3
    if num_all%21==0:
        print(convert(i, 6))
