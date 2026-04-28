from math import *


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'\files\27_B_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
            stars.append(dots[-1])

cluster_1 = [x for x in dots if x[1] > 22]
cl_1 = [x for x in stars if x[1] > 22]
cluster_2 = [x for x in dots if 16 < x[1] < 22]
cl_2 = [x for x in stars if 16 < x[1] < 22]
cluster_3 = [x for x in dots if x[1] < 15]
cl_3 = [x for x in stars if x[1] < 15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

B1 = dist(center_1, center_3) * 10000

dist_12 = max(dist(a, b) for a in cl_1 for b in cl_2)
dist_13 = max(dist(a, b) for a in cl_1 for b in cl_3)
dist_23 = max(dist(a, b) for a in cl_2 for b in cl_3)
B2 = max(dist_12, dist_13, dist_23) * 10000

print(B1, B2)
