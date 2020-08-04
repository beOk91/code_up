arr=[0 for i in range(10)]
arr2=[0 for i in range(1001)]
average,frequency=0,0
for i in range(10):
    arr[i]=int(input())
    arr2[arr[i]]+=1
    average+=arr[i]/10

for i in range(1001):
    if arr2[frequency]<arr2[i]:
        frequency=i
print("{}\n{}".format(int(average),frequency)) 