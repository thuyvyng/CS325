from heapq import heappush, heappop, heapify
from collections import defaultdict

def pair_check(pair):
    if pair in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C'), ('G','U'),('U','G')]: return True
    return False

def best(DNA):
    length = len(DNA)
    opt = defaultdict(int)
    back = defaultdict(int)

    def solution(i,j):
        if i == j:
            return "."
        if i > j:
            return ""
        k = back[i,j]
        if k == -1:
            return "(%s)" % solution(i+1, j-1)
        else:
            return solution(i,k) + solution(k+1,j)

    def _best(i,j):
        if (i,j) in  opt:
            return opt[i,j]
        current = -1
        for k in range(i,j):
            if current < _best(i,k) + _best(k+1,j):
                current = _best(i,k) + _best(k+1,j)
                back[i,j] = k
        if pair_check((DNA[i],DNA[j])) == True:
            if current < _best(i+1,j-1)+1:
                current = _best(i+1,j-1)+1
                back[i,j] = -1
        opt[i,j] = current
        return current

    for i in range(length):
        opt[i,i] = 0
        opt[i,i-1] = 0
    return _best(0,length-1), solution(0,length-1)

def total(DNA):
    def _total(i,j):
        if (i,j) in  opt: return opt[i,j]
        current = 0
        for k in range(i,j):
            if pair_check((DNA[k],DNA[j])) == True:
                current += _total(i,k-1) * _total(k+1,j-1)
        current += _total(i,j-1)
        opt[i,j] = current
        return opt[i,j]

    opt = defaultdict(int)
    length = len(DNA)
    for i in range(length):
        opt[i,i] = 1
        opt[i,i-1] = 1
    return _total(0,length-1)

def kbest(DNA,k):
    def _kbest(i,j):
        if (i,j) in opt: return opt[i,j]
        def trypush_b(s,p,q):
            if p < len(opt[i,s]) and q < len(opt[s+1,j]) and (s,p,q) not in visited:
                heappush(h, (-(opt[i,s][p][0] + opt[s+1,j][q][0]),(s,p,q)))
                visited.add((s,p,q))
        def trypush_pair(p):
            if p < len(opt[i+1,j-1]):
                heappush(h, (-(opt[i+1,j-1][p][0] + 1),(p,)))

        visited = set()
        h = []
        check_duplicates = set()

        for split in range(i,j):
            _kbest(i,split)
            _kbest(split+1,j)
            trypush_b(split,0,0)
        if pair_check((DNA[i],DNA[j])) == True:
            _kbest(i+1,j-1)
            trypush_pair(0)
        #for counter in range(k):
        while len(opt[i,j]) < k:
            if h == []: break
            score, index = heappop(h)
            try:
                s,p,q = index
                if ("%s%s" % (opt[i,s][p][1],opt[s+1,j][q][1])) not in check_duplicates:
                    opt[i,j].append((-score, "%s%s" % (opt[i,s][p][1],opt[s+1,j][q][1])))
                    check_duplicates.add(("%s%s" % (opt[i,s][p][1],opt[s+1,j][q][1])))
                trypush_b(s,p+1,q)
                trypush_b(s,p,q+1)
            except:
                p = index[0]
                if ("(%s)" % opt[i+1,j-1][p][1]) not in check_duplicates:
                    opt[i,j].append((-score, "(%s)" % opt[i+1,j-1][p][1]))
                    check_duplicates.add(("(%s)" % opt[i+1,j-1][p][1]))
                trypush_pair(p+1)


        return opt[i,j]


    length = len(DNA)
    opt = defaultdict(list)
    for i in range(length):
        opt[i,i] = [(0,'.')]
        opt[i,i-1] = [(0,'')]
    return _kbest(0,length-1)
