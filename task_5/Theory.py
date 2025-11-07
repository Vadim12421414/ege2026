#Системы счисления

#Двоичная система
N=25
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
print(bin(N)[2:])

# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
print(f'{N:b}')

#Восьмеричная система
print(oct(N)[2:])
print(f'{N:0}')

#Шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')

#Перевод в любую систему(2 <= sys <=9)
def convert(num, sys):
    res=''
    while num !=0:
        res=res+str(num%sys)
        num=num//sys
    return res[::-1]
print(convert(25, 3))

#-------------------------------------

#Перевод в любую систему(2 <= sys <=36)
from string import printable as alph
def convert(num, sys):
    res=''
    while num !=0:
        res=res+alph[num%sys]
        num=num//sys
    return res[::-1]
print(convert(25, 3))

#Перевод в 10 систему
num_bin='101'
num_tri='121'
num_hex='fa8'
print(int(num_bin, 2))
print(int(num_hex, 16))
print(int(num_tri, 3))


