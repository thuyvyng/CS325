def sorted(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x>= pivot]
    return sorted(left) + [pivot] + sorted(right)

def find(arr):
    arr = sorted(arr)
    triples = []
    n = len(arr)

    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] - arr[k] == 0):
                    triples.append((arr[i],arr[j],arr[k]))



    return triples



print(find([1, 4, 2, 3, 5]))
