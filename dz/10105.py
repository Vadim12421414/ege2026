with open('../files/24_10105.txt') as file:
    s = file.readline()

target = 100
max_len = 0


for start in range(len(s)):
    count_T = 0
    for end in range(start, len(s)):
        if s[end] == 'T':
            count_T += 1
        if count_T == target:
            max_len = max(max_len, end - start + 1)
        if count_T > target:
            break

print(max_len)