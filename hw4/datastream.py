import heapq

def ksmallest(k, array):
    negative_array = [i * -1 for i in array]
    k_array = negative_array[0:k]
    heapq.heapify(k_array)
    for i in range(k,len(array)):
        if k_array[0] < negative_array[i]:
            heapq.heapreplace(k_array, negative_array[i])
    fin_array = [i * -1 for i in k_array]
    x = sorted(fin_array)
    return x



#Test Cases
print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))   #[2, 3, 5, 7]
print(ksmallest(3, range(1000000, 0, -1)))           #[1,2,3]
