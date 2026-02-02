#from fnmatch import fnmatch
#for n in range(124065-124065%161, 10**8+1, 161):
 #   if fnmatch(str(n), '12*4?65'):
#        print(n, n//161)
##########################################
from itertools import product, repeat
from string import printable
ans=[]
for v in printable[10]:
    for l in range(0, 3):
        for z in product(printable[:10], repeat=l):
            num=int(f'12{''.join(z)}4{v}65')
            if num%161==0 and num<=10**8:
                ans.append([num, num%161])
for i in sorted(num):
    print(*i)