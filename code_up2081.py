arr=[]
for i in range(9):
    arr.append(int(input()))
arr2=arr.copy()
arr2.sort(reverse=True)
print(arr2[0])
print(arr.index(arr2[0])+1)