################################################
#### Bubble sort
################################################
def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1,i,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]

#####
a_bubble = [4,-2,10,0,5,8,12,9]
#####
print('Sorting ', a_bubble, 'with bubble sort') 
bubblesort(a_bubble)
print('We get ', a_bubble)



################################################
#### Insertionsort
################################################
def insertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while i>=0 and arr[i] > key:
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key

#####
a_insertionsort = [9,-1,5,0,16,8,10,22,-5]
#####
print('\nSorting ', a_insertionsort, 'with insertion sort') 
insertionSort(a_insertionsort)
print('We get ',a_insertionsort)



################################################
#### Mergesort
################################################
def merge(arr,p,q,r):
    l_arr = list(arr[p:q+1])
    r_arr = list(arr[q+1:r+1])
    i = j = 0
    for k in range(p,r+1):
        if(i<len(l_arr) and j<len(r_arr)):
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
        else:
            if i<len(l_arr):
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
        

def mergeSort(arr,p,r):
    if p<r:
        q = (p+r)//2
        mergeSort(arr,p,q)
        mergeSort(arr,q+1,r)
        merge(arr,p,q,r)

#####
a1_merge = [5,7,6,4,1,11,2,30,2,4,5,7,1,2,3,6,-1,56,19]

#print('\nThe result of applying merge to ', a1_merge, 'with p=8, q=11 and r=15 is')
#merge(a1_merge,8,11,15)
#print(a1_merge)
#####

#####
a2_merge = [10,15,9,2,7,14,1,11,25,0,33]
#####

#####
a3_merge = []
#####

print('\nSorting ', a2_merge, 'with mergesort') 
mergeSort(a2_merge,0,len(a2_merge)-1)
print('We get ',a2_merge)



################################################
#### Quicksort
################################################
def partition(arr,p,r):
    x = arr[r]
    i = p-1
    for j in range(p,r):
        if arr[j]<= x:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return (i+1)


def quickSort(arr,p,r):
    if p<r:
        q = partition(arr,p,r)
        quickSort(arr,p,q-1)
        quickSort(arr,q+1,r)

#####
#a0_quicksort = [2,8,7,1,3,5,6,4]
#a1_quicksort = [10,9,8,7,6,5,4,3]
a2_quicksort = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
#a3_quicksort = [8,8,8,8,8,8,8,8]
#####

print('\nSorting ', a2_quicksort, 'with quicksort') 
quickSort(a2_quicksort,0,len(a2_quicksort)-1)
print('We get ', a2_quicksort)
