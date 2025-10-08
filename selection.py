import time

def selection(arr):
    count=0
    start = time.time()
    for i in range(len(arr)):
        minimum = arr[i]
        minimum_index = i
        for j in range(i, len(arr)):
            if minimum > arr[j]:
                minimum = arr[j]
                minimum_index = j
            count+=1
        arr[i] , arr[minimum_index]= minimum, arr[i]
    end = time.time()
   # print(arr)
    return [end-start, count]