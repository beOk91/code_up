n_list=input().strip().split()
arr=[0]*10
for i in range(10):
    sum1=0
    for element in n_list[i]:
        sum1+=int(element)
    arr[i]=sum1
print(max(arr),min(arr))
