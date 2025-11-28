def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
num_25=3*3125**8+2*625**7-4*625**6+3*125**5-2*25*4-2025
r=convert(num_25, 25)
r=r.count('0')
print(r)



