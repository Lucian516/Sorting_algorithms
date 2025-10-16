
arr = [8,2,7,4,5,3,2,6,1, 2, 8, 6, 456, 45, 12, 21, 78, 34, 23, 90, 123, 11]

def partition(left, right):
    mid = int((left+right)/2)
    pivot = arr[mid]
    first = True
    second = True
    j = mid
    i = mid
    while(i<=right and j>=left):
        if arr[i]<pivot: second = False
        if arr[j]>pivot: first = False
        if (not first) and (not second):
            first = True
            second = True
            arr[i], arr[j]=arr[j], arr[i]
            i+=1
            j-=1 
        if (first==True): j-=1
        if (second==True): i+=1
    if (left<mid): 
        partition(left, mid-1)
    if (right>mid):
        partition(mid+1, right)
        
n = len(arr)
partition(0, n-1)
print (arr)