def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
l=[12,5,47,534,65,2344,676,4,567,43,57,5,345,65,3,45]
result=bubblesort(l)
print(result)