cnt=int(input())
arr=[]
for i in range(cnt):
    num=int(input())
    if num==0:
        del arr[len(arr)-1]
    else:
        arr.append(num)
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)