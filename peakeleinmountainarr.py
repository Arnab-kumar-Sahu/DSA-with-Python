def peakele(arr):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid - 1] < arr[mid] or arr[mid] < arr[mid + 1]:
            s = mid + 1
        else:
            e = mid - 1
l=[1,2,3,4,5,6,3,2]
res=peakele(l)
print(res)