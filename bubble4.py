import time
import random

def bubble(arr):
    count=0
    start = time.time()
    direction = True
    change = True
    last_changed_left=0
    last_changed_right=len(arr)-1
    while(change):
        change=False
        if direction: 
            for i in range(last_changed_left, last_changed_right):
                if arr[i]>arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    change=True
                    last_changed_right=i
                count+=1
            direction=False
        else:
            for i in range(last_changed_right, last_changed_left, -1):
                if arr[i]<arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    change=True
                    last_changed_left=i
                count+=1
            direction = True
    end = time.time()
    print (arr)
    return [end-start, count]