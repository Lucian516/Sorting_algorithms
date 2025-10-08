import time

def bubble(arr):
    count=0
    start = time.time()
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            count+=1

    end = time.time()
    #print (arr)
    return [end-start, count]

def bubble2(arr):
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

def bubble3(arr):
    count=0
    start = time.time()
    for i in range(len(arr)):
        change=False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                change=True
            count+=1
        if change==False:
            break

    end = time.time()
    #print (arr)
    return [end-start, count]

def bubble4(arr):
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
    #print (arr)
    return [end-start, count]