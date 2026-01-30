from fnmatch import fnmatch

for n in range(154682, 10 ** 11 + 1, 154682):
    if fnmatch(str(n), '*192?3*68'):
        print(n, n // 154682)
