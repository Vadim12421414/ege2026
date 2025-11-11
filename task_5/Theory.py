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

#Срезы
data='123456789'

#Извлечение первых двух символов
print(data[:2])

#Извлечение без первых двух символов
print(data[2:])

#Извлечение последних двух символов
print(data[-2:])

##Извлечение без последних двух символов
print(data[:-2])

#Сумма цифр числа
#Двоичная сисема
num1='1010'
sum1=num1.count('1')

#Любая система до 10(включительно)
num2='122'
sum2=sum(map(int, num2))

#Любая система до 36 (включительно)
num3='a'
sum3=sum(map(lambda x: int(x, 36), num3))
print(int(num3, 36))


