import random 
import time

#arr = [8,2,45, 12, 21, 78, 34, 123, 11, 56, 3, 7, 19]
count=0

def pivotselect(arr, i, j):
    a = random.randint(i, j)
    b = random.randint(i, j)
    c = random.randint(i, j)
    return sorted([arr[a], arr[b], arr[c]])[1]

def partition(arr, left, right, pivot):
    global count
    while(left<=right):
        while(arr[left]<pivot): 
            count+=1 
            left+=1
        while(arr[right]>pivot): 
            count+=1
            right-=1
        if (left<=right):
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    return left

def quicksort(arr, left, right):
    if (left<right):
        pivot = pivotselect(arr, left, right)
        mid = partition(arr, left, right, pivot)
        quicksort(arr, left, mid-1)
        quicksort(arr, mid, right)
def sort(arr):
    start = time.time()
    quicksort(arr, 0, len(arr)-1)
    end = time.time()
    return [end-start, count]
#sort(arr)
#print (arr)