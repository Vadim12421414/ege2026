from math import dist
def edge(cluster):
    res = []
    for dot in cluster:
        sum_dis = sum(dist(dot, dot2) for dot2 in cluster)
        res.append([sum_dis, dot])
    return max(res)[1]
with open('r/27A_27590.txt/') as file:
    dots=[list(map(float, i.replace(',', '.').split())) for i in file]
eps=1
clusters=[]
while dots:
    cluster=[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d)<eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)
