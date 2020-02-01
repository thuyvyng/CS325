# from collections import defaultdict
#
# def _order(n,edges):
#     adjlist = defaultdict(list)
#     indegree = defaultdict(int)
#
#     for u, v in edges: # u->v
#         adjlist[u].append(v)
#         indegree[v] += 1
#
#     stack = []
#     for u in range(n):
#         if indegree[u] == 0:
#             stack.append(u)
#     while stack != []:
#         u = stack.pop()
#         yield u
#         for v in adjlist[u]:
#             indegree[v] -= 1
#             if indegree[v] == 0:
#                 stack.append(v)
#
# def order(n,edges):
#     return list(_order(n,edges))
#
#
# x = order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
# print(x)

###

from collections import defaultdict
import operator

def order(n, edges):
    def _order(n,edges):
        adjlist = defaultdict(list)
        indegree = defaultdict(int)

        for u, v in edges: # u->v
            adjlist[u].append(v) #where can 'u' go
            indegree[v] += 1     #how many things go into v/ how many pre-prerequisites
        stack = []
        for u in range(n):      #for how many nodes
            if indegree[u] == 0: stack.append(u)
        while stack != []:
            u = stack.pop()     #take the class and then 'return'/yield it
            yield u
            for v in adjlist[u]:
                indegree[v] -= 1 #since we have taken 'u' it is no longer a prereq for v
                if indegree[v] == 0: stack.append(v)
    return list(_order(n,edges))


def longest(nodes, edge):
    if edge == []: return 0, []

    back = defaultdict(list)
    len_path = defaultdict(int)
    top = order(nodes,edge)

    for u in top:
         for u,v in edge:
             if len_path[v] < len_path[u]+1:
                 len_path[v] = len_path[u]+1
                 back[v] = back[u][:]
                 back[v].append(u)

    largest = max(len_path.items())[0]
    back[largest].append(largest)
    return len(back[largest])-1, back[largest]
