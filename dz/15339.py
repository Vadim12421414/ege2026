from re import *

with open('../files/24_15339.txt') as file:
    data = file.readline()

    new_data = ''
    for i in data:
        if i in 'ABC':
            new_data += 'L'
        if i in '6789':
            new_data += 'D'

pattern = r'(LD|DL)+'

matches = [match.group() for match in finditer(pattern, new_data)]
print(len(max(matches, key=len)))
