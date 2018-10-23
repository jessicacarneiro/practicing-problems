from random import random
from math import floor

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


def swap(arr,index1,index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def partition(arr,left,right,pivot_index):
    pivot_value = arr[pivot_index]
    swap(arr,right,pivot_index) # move pivot to end
    store_index = left
    
    for i in range(left,right):
        if arr[i] < pivot_value:
            swap(arr,store_index,i)
            store_index = store_index + 1
    
    swap(arr,right,store_index) # move pivot to its final place
    return store_index

''' Returns the n-th smallest element of list within [left,right]
    The search space within the array is changing for each round
    - but the list is still the same size. Thus, n does not need
    to be updated with each round.
'''
def select(arr,left,right,n):
    if left == right:
        return arr[left]
    pivot_index = left + int(floor(random() % (right - left + 1)))
    pivot_index = partition(arr,left,right,pivot_index)
    
    # The pivot is in its final sorted position
    if n == pivot_index:
        return arr[n]
    elif n < pivot_index:
        return select(arr,left,pivot_index-1,n)
    else:
        return select(arr,pivot_index+1,right,n)
    
median = select(arr,0,n-1,n/2)
print median