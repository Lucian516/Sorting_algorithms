import time
import random

arr = [random.randint(0, 1000**2) for x in range(100)]

def threesmooth(N):
    S = [1]
    i2 = 0  # current index in 2S
    i3 = 0  # current index in 3S
    while S[len(S)-1]<N:
        n2 = 2 * S[i2]
        n3 = 3 * S[i3]
        S.append(min(n2, n3))
        i2 += n2 <= n3
        i3 += n2 >= n3
    return S
    
def shellsort(arr):
    sequence = threesmooth(len(arr))
    sequence.reverse()
    count=0
    start = time.time()
    for i in range(len(sequence)):
        gap = sequence[i]
        for k in range(0, len(arr), gap):
            j = k
            while j-gap>=0 and arr[j]<arr[j-gap]:
                arr[j-gap], arr[j] = arr[j], arr[j-gap]
                count+=1
                j-=gap

    end = time.time()
    #print (arr)
    return [end-start, count]

x = shellsort(arr)

for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        print("ASDFASDFASF")
        break