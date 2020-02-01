
def best(capacity, pairs):
    w, v = zip(*pairs)
    def _best(capacity, weight, value):
        arr = [0 for i in range(capacity+1)]
        counter = [0]*len(weight)


        for i in range(capacity+1):
            for j in range(len(value)):
                if weight[j] <= i :
                    counter[j] += 1
                    arr[i] = max(arr[i], arr[i-weight[j]] + value[j])
        print(arr)
        return arr[capacity]
    return _best(capacity, w, v)

print(best(3, [(1, 5), (1, 5)]))
