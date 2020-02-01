def num_inversions(array):
    test = _mergesort(array)
    return test[1]

def _mergesort(array):
    if len(array) == 1:
        return array, 0
    else:
        midpoint = len(array)//2
        left = array[:midpoint]
        right = array[midpoint:]
        left, left_inversions = _mergesort(left)
        right, right_inversions = _mergesort(right)
        c = []

        l = 0
        r = 0

        inversions = right_inversions + left_inversions

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            c.append(left[l])
            l += 1
        else:
            c.append(right[r])
            r += 1
            inversions += (len(left)-l)
    c += left[l:]
    c += right[r:]
    return c, inversions

test = [2, 4, 1, 3]
print(num_inversions(test))
