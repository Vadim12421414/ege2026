def convert(num, sys):
    res=''
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
num_5=15625**16-3125**3*25**19+625**4-2005
num_5=convert(num_5, 5)
r=num_5.count('0')
print(r)
