import itertools
import random

def qselect(k,a):
    if a == [] or k>len(a) or k==0:
        return []
    else:
        #i=random.randint(0,len(a)-1)
        #a[0],a[i]=a[i],a[0]
        pivot=a[0]

        left = [x for x in a if (x[0]+x[1]) < (pivot[0]+pivot[1]) ]

        splitP=len(left)
        if splitP==k-1:
            return pivot

        elif splitP>k-1:
            return qselect(k,left)

        else:
            right = [x for x in a[1:] if (x[0]+x[1]) >= (pivot[0]+pivot[1])]
            return qselect(k-(splitP+1),right)

def nbesta(a,b):
    len_a = len(a)
    list = []
    sumlist = []

    for i in itertools.product(a,b):
        list.append(i)

    sumlist = [sum(tup) for tup in list]
    x = zip(sumlist, list)
    x = set(x)
    x = sorted(x)

    list_final = x[0:len_a]
    first,sec = zip(*list_final)
    return sec

def nbestb(a,b):
    len_a = len(a)
    list = []
    sumlist = []

    for i in itertools.product(a,b):
        list.append(i)

    for i in range(len_a):
        sumlist.append(qselect(i+1,list))


    return sumlist

def nbestc(a,b):
    return

#Test
a, b = [4, 1, 5, 3], [2, 6, 3, 4]
#print(nbesta(a, b))
print(nbestb(a, b))
