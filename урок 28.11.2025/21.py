def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans_n=[]
ans_r=[]
ans=[]
for n in range(1, 100_000):
    r = convert(n, 4)
    if sum(map(int, r))%3==0:
        r=r.replace('0', '*')
        r=r.replace('2', '0')
        r=r.replace('*', '2')
        r+='32'+r
    else:
        r=r[0]+'10'+r[3:]+'33'
    r=int(r, 4)

#     if r>320:
#         ans_r.append(r)
#         ans_n.append(n)
# min_r=min(ans_r)
# for i in range(len(ans_r)):
#     if ans_r[i] == min_r:
#         print(ans_n[i])
    if r==335:
        ans.append(n)
print(max(ans))





