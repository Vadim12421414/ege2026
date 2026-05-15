from re import *

with open('../files/24_15339.txt') as file:
    data = file.readline()

    new_data = ''
    for i in data:
        if i in 'ABC':
            new_data += 'b'
        if i in '6789':
            new_data += '0'

pattern = r'b?(b0|0b)+0?'

matches = [match.group() for match in finditer(pattern, new_data)]
print(len(max(matches, key=len)))
