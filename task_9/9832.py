with open(r'Files/9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]
for line in data:
    amount = [line.count(i) for i in line]
    if amount.count(2) == 4 and amount.count(1) == 3:  # можно записать по другому if sorted(amount)==[1,1,1,2,2]
       if line.count(max(line))==1:
           print(sum(line))
           break