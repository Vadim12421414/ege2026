from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'./files/23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster_1_A = [dot for dot in dots if dot[1] > 5]
cluster_2_A = [dot for dot in dots if dot[1] < 5]
center_1_A = center(cluster_1_A)
center_2_A = center(cluster_2_A)
print((max(center_1_A[0], center_2_A[0])) * 10000)
print((max(center_1_A[1], center_2_A[1])) * 10000)
with open('r/files/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster_B_1 = [d for d in dots if 0 < d[1] < 15]
cluster_B_2 = [d for d in dots if 15 < d[1] < 21]
cluster_B_3 = [d for d in dots if 21 < d[1] < 30]
clusters_B = [cluster_B_1, cluster_B_2, cluster_B_3]

max_cluster = center(max(clusters_B, key=len))
min_cluster = center(min(clusters_B, key=len))

print((max_cluster[0] - min_cluster[0]) * 10_000)
print((max_cluster[1] - min_cluster[1]) * 10_000)