num=int(input())
arr=[]
for i in range(num):
    arr.append(float(input()))
arr2=[0]*num
arr2[0]=0
for i in range(num):
    if i==0:
        arr2[i]=arr[i]
    elif arr2[i-1]*arr[i]<arr[i]:
        arr2[i]=arr[i]
    else:
        arr2[i]=arr2[i-1]*arr[i]
print("%.3f" %round(max(arr2),3))