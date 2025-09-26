def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
l=[1,2,43,6,75,5,87,898,56,45,86]
res=selectionsort(l)
print(res)