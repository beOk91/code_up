def selectionSort(myList):
    for i in range(len(myList)):
        minIndex=i
        for j in range(i+1,len(myList)):
            if myList[minIndex]>myList[j]:
                minIndex=j
        myList[i],myList[minIndex]=myList[minIndex],myList[i]
    return myList

num=int(input())
arr=[0]*num
for i in range(num):
    arr[i]=int(input())
selectionSort(arr)
for element in arr:
    print(element)