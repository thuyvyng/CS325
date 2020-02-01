from collections import defaultdict
from heapdict import heapdict

def shortest(n, edges):
    if edges == []: return None
    def solution(v):
        if v not in back:
            return [v]
        return solution(back[v]) + [v]

    adjlist = defaultdict(list)
    for u, v, c in edges:
        adjlist[u].append((v,c))
        adjlist[v].append((u,c))

    back = {}
    visited = set()

    path_weight = defaultdict(lambda: float("inf"))
    path_weight[0] = 0


    h = heapdict()
    h[0] = 0
    while len(h) > 0:
        u_item = h.popitem()
        if u_item[0] == n-1: break
        visited.add(u_item[0])
        for v,c in adjlist[u_item[0]]:
            if v not in visited:
                if path_weight[v] > path_weight[u_item[0]] + c:
                    path_weight[v] = path_weight[u_item[0]] + c
                    back[v] = u_item[0]
                    h[v] = path_weight[v]

    if (path_weight[n-1] == float("inf")): return None
    else: return path_weight[n-1], solution(back[n-1])+[n-1]
