from string import printable
def convert(num, sys):
    res=''
    while num:
        res+=printable[num%sys]
        num//=sys
    return res[::-1]

num_10=2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
num_27=convert(num_10, 27)
cnt=0
for i in num_27:
    if int(i, 27)>9:
        cnt+=1
print(cnt)

###

cnt_3=0
for i in num_27:
    if i in printable[10:27]
        cnt_3+=1
print(cnt_3)


