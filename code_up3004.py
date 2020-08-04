def binarysearch(arr,target,first,last):
    if first>last:
        return 1
    mid=int((first+last)/2)
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binarysearch(arr,target,first,mid-1)
    else:
        return binarysearch(arr,target,mid+1,last)

num=int(input())
arr=list(map(int,input().strip().split()))
arr2=sorted(arr)
for i in range(num):
    print(binarysearch(arr2,arr[i],0,num-1),end=" ")
for i in range(num):
    print(arr2.index(arr[i]),end=" ")

"""
for i in range(num):
    idx=arr[i]
    print(arr2.index(idx),end=" ")
"""