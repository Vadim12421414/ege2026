from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append(sum_dist, dot)
    return min(res)[1]


with open(r'...') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            stars.append(dots[-1])
cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]
center1 = center(cluster1)
center2 = center(cluster2)
stars1 = [d for d in stars if d[1] > 8]
stars2 = [d for d in stars if d[1] < 8]
ans = []
for s in stars1:
    ans.append(dist(center1, s))
for s2 in stars2:
    ans.append(dist(center2, s2))
print(min(ans) * 10000, max(ans) * 10000)
################################## можно и так
cluster_1 = [[d for d in dots if d[1] > 8],
             [d for d in stars if d[1] > 8]]
cluster_2 = [[d for d in dots if d[1] < 8],
             [d for d in stars if d[1] < 8]]
clusters = [cluster_1, cluster_2]

A1 = min(dist(center(cl[0]), s) for cl in clusters for s in cl[1])
A2 = max(dist(center(cl[0]), s) for cl in clusters for s in cl[1])
