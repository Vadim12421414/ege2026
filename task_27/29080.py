from math import *


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'./files/27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '3' and data[0] == 'L':
            stars.append(dots[-1])

cluster_1 = [x for x in dots if x[1] > 10]
cluster_2 = [x for x in dots if x[1] < 10]

minn = []
maxx = []
if len(cluster_1) > len(cluster_2):
    minn, maxx = cluster_2, cluster_1
else:
    minn, maxx = cluster_1, cluster_2

A1 = max(dist(center(minn), i) for i in stars) * 10000
A2 = max(dist(center(maxx), i) for i in stars) * 10000
print(A1, A2)