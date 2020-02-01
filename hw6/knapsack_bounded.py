#Bottom Up
# def best(capacity, items):
#     w,v,c = zip(*items)
#     arr = [[0 for x in range(len(items)+1)] for x in range(capacity+1)]
#
#     def _best(capacity,weight,value,copies,a,items):
#         return_list = [0 for x in range(len(copies))]
#
#         for w in range(capacity +1):
#             for i in range(len(items)+1):
#                 #for me in range(copies[i-1]):
#                     if i == 0 or capacity == 0: a[w][i] = 0
#                     elif weight[i-1] > w: a[w][i] = a[w][i-1]
#                     else:
#                         return_list[i-1] += 1
#                         a[w][i] = (max(value[i-1] + a[w-weight[i-1]][i-1], a[w][i-1]))
#         return a[w][len(copies)]
#     return _best(capacity, w,v,c,arr,items)


# #Top Down
# def best(capacity, items):
#     w,v,c = zip(*items)
#     woo = {}
#     def _best(capacity,n, w, v, c):
#         if capacity not in woo:
#             if capacity == 0 or n == 0:
#                 result = 0
#             elif w[n] > capacity:
#                 result = _best(capacity, n-1, w,v,c)
#             else:
#                 result = max( _best(capacity,n-1,w,v,c), _best(capacity-w[n],n-1,w,v,c) + v[n])
#
#             woo[capacity] = result
#         return woo[capacity]
#
#     return _best(capacity, len(items)-1, w,v,c)

# def best(capacity, items):
#     w,v,c = zip(*items)
#     items = sum( ([(wt, val)]*n for wt, val,n in item), [])
#     arr = [[-1 for x in range(len(items))] for x in range(capacity)]
#
#     def _best(capacity,n, w, v, c):
#         if arr[capacity-1][n-1] != -1:
#             return arr[capacity-1][n-1]
#         if capacity == 0 or n == 0:
#             result = 0
#         if w[n-1] > capacity:
#             result = _best(capacity, n-1, w,v,c)
#         else:
#             result = max( _best(capacity,n-1,w,v,c), _best(capacity-w[n-1],n-1,w,v,c) + v[n-1])
#         arr[capacity-1][n-1] = result
#         return result
#
#     return _best(capacity, len(items), w,v,c)
# #Top Down
# def best(limit, it):
#     items = sum( ([(wt, val,n)]*n for wt, val,n in it), [])
#     table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]
#
#     for j in range(1, len(items) + 1):
#         wt, val, n = items[j-1]
#         for w in range(1, limit + 1):
#             if wt > w:
#                 table[j][w] = table[j-1][w]
#             else:
#                 table[j][w] = max(table[j-1][w], table[j-1][w-wt] + val)
#
#     result = []
#     w = limit
#
#     for j in range(len(items), 0, -1):
#         was_added = table[j][w] != table[j-1][w]
#
#         if was_added:
#             wt, val, n = items[j-1]
#             print(items[j-1])
#             result.append(items[j-1])
#             w -= wt
#
#
#     return sum(w[1] for w in result)

# def best(capacity, items):
#     oof = {}
#     def _best(capacity, items, n):
#         item = (capacity, n)
#
#         if n < 0 or capacity < 0: oof[item] = (0,0)  #base case
#
#         if item not in oof:
#             w, v, qty = items[n]
#             best_v, best_list = 0, []
#
#             for i in range(0, qty + 1):
#                 if capacity - i * w < 0: break
#
#                 # val, taken = _best(capacity - i * w,items, n - 1
#                 # if val + i * v > best_v:
#                 #     best_v = val + i * v
#                 #     best_list = taken[:]
#                 #     best_list.append(i)
#
#             oof[item]= [best_v, best_list]
#         return oof[item]
#     return _best(capacity,items, len(items)-1)

def best(capacity, items):
    oof = {}
    def _best(capacity, n):
        item = (capacity, n)
        if n < 0 or capacity < 0: oof[item] = (0,0)  #base case
        if item not in oof:
            w, v, qty = items[n]
            best = (0, 0)

            for numcopies in range(0, qty + 1):
                #weightcopies = numcopies * w
                #valuecopies = numcopies * v

                if capacity <  numcopies * w: break

                bestvaluewithcopies = _best(capacity-(numcopies * w), n-1)[0] + (numcopies * v)
                if bestvaluewithcopies > best[0]: best = (bestvaluewithcopies,numcopies)


            oof[item]= best
        return oof[item]

    def trace(capacity):
        list = [0 for _ in range(len(items))]

        current_cap = capacity
        item_index = len(items)-1

        while oof[current_cap,item_index][0] > 0:
            if oof[current_cap,item_index][0] > oof[current_cap,item_index-1][0]:
                copies_c = oof[current_cap,item_index][1]
                list[item_index] += copies_c
                current_cap -= items[item_index][0] * copies_c
            item_index -= 1
        return list


    return _best(capacity, len(items)-1)[0], trace(capacity)


# def best(capacity, item):
#     items = sum( ([(wt, val)]*n for wt, val,n in item), [])
#     print(items)
#     table = [[0 for w in range(capacity + 1)] for j in range(len(items) + 1)]
#
#     for j in range(1, len(items) + 1):
#         wt, val = items[j-1]
#         for w in range(1, capacity + 1):
#             if wt > w:
#                 table[j][w] = table[j-1][w]
#             else:
#                 table[j][w] = max(table[j-1][w], table[j-1][w-wt] + val)
#
#     result = []
#     w = capacity
#     for j in range(len(items), 0, -1):
#         was_added = table[j][w] != table[j-1][w]
#
#         if was_added:
#             wt, val = items[j-1]
#             result.append(items[j-1])
#             w -= wt
#
#     print(table)
#     return
