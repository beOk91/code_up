def binarySearch(arr,value,first,last):
    mid=0
    while first<=last:
        mid=int((first+last)/2)
        if arr[mid]==value:
            return mid
        else:
            if value<arr[mid]:
                last=mid-1
            else:
                first=mid+1
    return -2
    """
    if first==end and arr[first]!=value:
        return -2
    elif arr[mid]==value:
        return mid
    elif value<arr[mid]:
        return binarySearch(arr,value,first,mid-1)
    else:
        return binarySearch(arr,value,mid+1,end)
    """

num1=int(input())
num1_list=list(map(int,input().strip().split()))
num2=int(input())
num2_list=list(map(int,input().strip().split()))

for i in range(num2):
    print(binarySearch(num1_list,num2_list[i],0,num1-1)+1,end=" ")