def longest(tree):
    _, result = _longest(tree)
    return result


def _longest(tree):
    if tree == []:
        return 0,0

    left_height, left_longest = _longest(tree[0])
    right_height, right_longest = _longest(tree[2])

    current_height = max(left_height,right_height) +1
    current_longest = left_height + right_height

    return current_height, max(current_longest, left_longest, right_longest)

def height(tree):
    return _longest(tree)

#Test Cases
test1 = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]
test2 = [[], 1, []]
test3 = [[[], 1, []], 2, [[], 3, []]]

print(longest(test1))
print(longest(test2))
print(longest(test3))
