from collections import defaultdict
import operator

def longest(n, edges):
    if edges == []: return 0, []
    back = defaultdict(list)
    len_path = defaultdict(int)
    def order(n,edges):
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
            for v in adjlist[u]:
                indegree[v] -= 1 #since we have taken 'u' it is no longer a prereq for v
                if indegree[v] == 0: stack.append(v)
                if len_path[v] < len_path[u]+1:
                    len_path[v] = len_path[u]+1
                    back[v] = back[u][:]
                    back[v].append(u)
    
        largest = max(len_path.items(), key=operator.itemgetter(1))[0]
        back[largest].append(largest)
        return len(back[largest])-1, back[largest]
    return order(n,edges)
