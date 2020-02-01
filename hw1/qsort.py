#ThuyVy Nguyen
#CS325 - HW1

def sort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]

    return [sort(left)] + [pivot] + [sort(right)]

def sorted(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x>= pivot]
    return sorted(left) + [pivot] + sorted(right)

#this helper function should return the subtree rooted at x where x is found
#pretty sure the return []s are wrong someone help me
def _search(tree,x):
    if x == tree[1]:
        return tree
    elif x > tree[1]:
        if tree[2] != []:
            return _search(tree[2],x)
        else:
            return tree[2]
    elif x < tree[1]:
        if tree[0] != []:
            return _search(tree[0],x)
        else:
            return tree[0]


#returns whether x is in tree
def search(t,x):
    if _search(t,x) == []:
        return False
    else:
        return True

#inserts x in place if its missing if not do nothing
def insert(t,x):
    location = _search(t,x)

    if location == []:
        location.append([])
        location.append(x)
        location.append([])

    return t
