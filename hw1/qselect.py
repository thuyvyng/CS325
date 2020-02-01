#ThuyVy Nguyen
#CS325 - HW1

import random


#highest number the pivot can be, finds randomized partiton
def randpartition(max):
    z = random.randrange(max);
    return z


#QuickSelect(#kth smallest element, array)
def qselect( k, array):

    def select(s_array, left, right, index):

        # base case = when the array has one element/has been reduced to one, so this has to be the pivot
        if right == left:
            return s_array[right]


        #else - choose a random pivot (randint includes left and right :) )
        pivot_index = random.randint(left, right)

        #switch the pivot with the first index (left) in the subarray
        s_array[left], s_array[pivot_index] = s_array[pivot_index],s_array[left]

        #put smaller numbers on the left, and bigger numbers on the right
        #index of pivot_position = left, and pivot_pos
        pivot_pos = left


        #range does not include the upper end so add one!, and dont include the pivot itself
        for w in range(left+1, right+1):
            #iterate through the array and check if its greater than pivot index (left)

            if s_array[w] < s_array[left]:
                #keeps track of how many to move it over later

                pivot_pos = pivot_pos + 1

                s_array[pivot_pos], s_array[w] = s_array[w], s_array[pivot_pos]



        #move pivot to correct pivot pivot_index

        s_array[pivot_pos], s_array[left] = s_array[left],s_array[pivot_pos]



        #do it to the left or right side, this is where it gets recursive
        if index == pivot_pos:
            return s_array[pivot_pos]
        elif index < pivot_pos:
            return select(s_array, left, pivot_pos - 1, index)
        else:
            return select(s_array, pivot_pos + 1, right, index)

    #      select(array, left, right, index)
    return select(array,0, len(array)-1,k-1)

print(qselect(2, [3, 10, 4, 7, 19]))
print(qselect(4, [11, 2, 8, 3]))
print(qselect(3, [11, 2, 8, 3]))
print(qselect(1, [11, 2, 8, 3]))
