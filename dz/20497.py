from math import *

with open(r'27.19.A_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


def uncentre(cluster):
    res = []
    for dot in cluster:
        sum_dis = sum(dist(dot, dot2) for dot2 in cluster)
        res.append([sum_dis, dot])
    return max(res)[1]


cluster_1 = [i for i in dots if i[0]<0 and i[1]<0]
cluster_2 = [i for i in dots if i[0]>0.5 and 0>i[1]>-5]
cluster_3 = [i for i in dots if i[0]>-1 and 7>i[1]>1]

center_1 = uncentre(cluster_1)
center_2 = uncentre(cluster_2)
center_3 = uncentre(cluster_3)

print(abs((center_1[0] + center_2[0]+center_3[0])) / 3 * 10000)
print(abs((center_1[1] + center_2[1]+center_3[1])) / 3 * 10000)

from math import *

with open(r'27.19.B_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


def uncentre(cluster):
    res = []
    for dot in cluster:
        sum_dis = sum(dist(dot, dot2) for dot2 in cluster)
        res.append([sum_dis, dot])
    return max(res)[1]


cluster_1 = [i for i in dots if i[0]<-35 and i[1]<33]
cluster_2 = [i for i in dots if -21>i[0]>-41 and i[1]>45]
cluster_3 = [i for i in dots if -9>i[0]>-25 and i[1]<38]
cluster_4 = [i for i in dots if 7>i[0]>-13 and i[1]>45]
cluster_5 = [i for i in dots if 18>i[0]>1 and i[1]<38]

center_1 = uncentre(cluster_1)
center_2 = uncentre(cluster_2)
center_3 = uncentre(cluster_3)
center_4 = uncentre(cluster_4)
center_5 = uncentre(cluster_5)

print(abs((center_1[0] + center_2[0]+center_3[0]+center_4[0]+center_5[0])) / 5 * 10000)
print(abs((center_1[1] + center_2[1]+center_3[1]+center_4[1]+center_5[1])) / 5 * 10000)


