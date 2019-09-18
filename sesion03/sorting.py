def partition(arr,p,r):
    x = arr[r]
    i = p-1
    for j in range(p,r):
        if arr[j]<= x:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    print(arr)
    return (i+1)


def quickSort(arr,p,r):
    if p<r:
        q = partition(arr,p,r)
        quickSort(arr,p,q-1)
        quickSort(arr,q+1,r)


a = [2,8,7,1,3,5,6,4]
#a = [10,9,8,7,6,5,4,3]
#a = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
#a = [8,8,8,8,8,8,8,8]

print('\nSorting ', a)
print(quickSort(a,0,len(a)-1))

  
 
