import time

def bubble(arr):
    count=0
    start = time.time()
    for i in range(len(arr)):
        change=False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                change=True
            count+=1
        if change==False:
            break

    end = time.time()
    #print (arr)
    return [end-start, count]