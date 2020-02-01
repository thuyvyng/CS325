import math

def bsts(n):
    top = math.factorial(2*n)
    bottom1 = math.factorial(n+1)
    bottom2 = math.factorial(n)
    bottom = bottom1 *bottom2
    return (int)(top/bottom)

print(bsts(2))
print(bsts(3))
print(bsts(5))
