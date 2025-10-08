import time

def insertion(arr):
    count=0
    start = time.time()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            count+=1

    end = time.time()
    #print (arr)
    return [end-start, count]