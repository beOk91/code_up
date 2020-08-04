def insertionSort(myList):
    for i in range(1,len(myList)):
        for j in range(0,i):
            if myList[i]<myList[j]:
                myList.insert(j,myList.pop(i))
    return myList
num=int(input())
num_list=[0]*num
for i in range(num):
    num_list[i]=int(input())
insertionSort(num_list)
for element in num_list:
    print(element)