import time

arr=[1, 2, 3, 5, 8, 10, 15, 10, 12, 4, 5]

def insertion(arr):
    count=0
    start = time.time()
    for i in range(len(arr)):
        j = i
        while j>0 and arr[j]<arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            count+=1
            j-=1

    end = time.time()
    #print (arr)
    return [end-start, count]

x = insertion(arr)