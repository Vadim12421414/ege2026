with open('r') as file:
    data = file.readline()
data=data.replace('ab', '*')
data=data.replace('ac', '*')
for i in 'abc':
    data=data.replace(i, ' ')
print(len(max(data, key=len)))