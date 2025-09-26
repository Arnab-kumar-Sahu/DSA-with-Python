def lowerbound(arr,k):
    s=0
    e=len(arr)-1
    lb=len(arr)
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>=k:
            e=mid-1
            lb=mid
        else:
            s=mid+1
    return lb
l=[1,2,3,4,5,5,5,5,5,6,6,6,6,6,6,6,7,8]
res=lowerbound(l,6)
print(res)
