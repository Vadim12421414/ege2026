from re import *

with open('../files/24_4602.txt') as file:
    data = file.readline()
    data = data.replace('O', 'A')
    data = data.replace('C', 'B')
    data = data.replace('D', 'B')

pattern = r'([B][A])+'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)
