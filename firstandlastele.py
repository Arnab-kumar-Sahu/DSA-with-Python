def firstlast(arr,k):
    s=0
    e=len(arr)-1
    f=-1
    l=-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==k:
            f=mid
            e=mid-1
        elif arr[mid]>k:
            e=mid-1
        else:
            s=mid+1
    s=0
    e=len(arr)-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==k:
            l=mid
            s=mid+1
        elif arr[mid]>k:
            e=mid-1
        else:
            s=mid+1
    return f,l
l=[1,2,3,4,4,4,4,4,4,5,5,6,6,6,7,7,8,8]
res=firstlast(l,4)
print(res)