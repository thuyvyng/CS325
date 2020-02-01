import bisect
def sorted(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x>= pivot]
    return sorted(left) + [pivot] + sorted(right)

def find(array, x, k):
    right = bisect.bisect(array,x)
    left = right -1

    indicies = []

    while( left >= 0 and right < len(array) and len(indicies)<k):
        if(x-array[left] <= array[right]-x):
            indicies.append(left)
            left -= 1
        else:
            indicies.append(right)
            right += 1

    while(len(indicies) <k and left>= 0):
        indicies.append(left)
        left -= 1

    while(len(indicies) <k and right < len(array)):
        indicies.append(right)
        right += 1

    indicies = sorted(indicies)
    return [array[element] for element in indicies]


# Test Cases
# print(find([1,2,3,4,4,7], 5.2, 2))
# print(find([1,2,3,4,4,7], 6.5, 3))
print(find([1,2,3,4,4,6,6], 5, 3))
