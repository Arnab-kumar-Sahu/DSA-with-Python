def binarysearch(arr,key):
    s=0
    e=len(arr)-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            s=mid+1
        else:
            e=mid-1
    return -1
l=[1,2,3,4,5,6,7,8]
res=binarysearch(l,6)
print(res)
