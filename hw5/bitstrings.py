numbs = {0:1, 1:2}
def num_no(n):
    if n not in numbs:
        numbs[n] = num_no(n-1) + num_no(n-2)
    return numbs[n]

numbs2 = {0:0, 1:0, 2:1, 3:3}
def num_yes(n):
    if n not in numbs2:
        numbs2[n] = num_no(n-1) + num_no(n-2)
    return numbs2[n]

print(num_no(3))
print(num_yes(3))
