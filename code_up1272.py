k,h=map(int,input().strip().split())
arr=[0]*(max(k,h) if max(k,h)%2==0 else max(k,h)+1)
idx=1
for i in range(0,max(k,h),2):
    arr[i]=idx
    arr[i+1]=idx*10
    idx+=1
print(arr[k-1]+arr[h-1])