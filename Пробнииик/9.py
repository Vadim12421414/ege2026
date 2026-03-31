with open(r'file/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt=0
for line in data:
    amount = [line.count(i) for i in line]
    if sorted(amount)==[1,1,1,1,2,2]:
        ne_pov=[i for i in data if line.count(i)%2!=0]
        pov=[i for i in data if line.count(i)%2==0]
        for i in pov:
            if sum(i)>=sum(ne_pov):
                cnt+=1
print(cnt)
