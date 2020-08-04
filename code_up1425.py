n,c=map(int,input().strip().split())
arr=list(map(int,input().strip().split()))
arr.sort()
result=""
for i in range(n):
    if c==1 or (i>0 and (i+1)%(c)==0):
        result=result+str(arr[i])+" "
        if i!=n-1:
            result+="\n"
    else:
        result=result+str(arr[i])+" "
print(result)