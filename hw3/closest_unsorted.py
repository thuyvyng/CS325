import random

#Use quicksort to make sure values are printed in correct order
def sorted(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x>= pivot]
    return sorted(left) + [pivot] + sorted(right)

#dr. huangs code for qselect
def qselect( k, a):
    if a == [] or k>len(a) or k==0:
        return []
    else:
        i=random.randint(0,len(a)-1)
        a[0],a[i]=a[i],a[0]
        pivot=a[0]
        left = [x for x in a if x < pivot ]

        splitP=len(left)
        if splitP==k-1:
            return pivot

        elif splitP>k-1:
            return qselect(k,left)

        else:
            right = [x for x in a[1:] if x >= pivot]
            return qselect(k-(splitP+1),right)



#Given an array A of n numbers, a query x, and a number k,
#   find the k numbers in A that are closest (in value) to x.
def find(array, x, k):
    subtract = [abs(x-element) for element in array]
    sub = [abs(x-element) for element in array]
    max = qselect(k, subtract)
    indicies = []

    for index, value in enumerate(sub):
        if value < max:
            indicies.append(index)

    for i, v in enumerate(sub):
        if (v == max) and (len(indicies) < k):
            indicies.append(i)

    indicies = sorted(indicies)
    return [array[element] for element in indicies]


print(find([4,1,3,2,7,4], 5.2, 2)==[4,4])
print(find([4,1,3,2,7,4], 6.5, 3)==[4,7,4])
print(find([5,3,4,1,6,3], 3.5, 2)==[3,4])
