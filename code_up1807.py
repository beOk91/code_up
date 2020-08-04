def f(num):
    if num==1:
        return [1]
    elif num%2==1:
        return f(num*3+1)+[num]
    else:
        return f(num//2)+[num]
a,b=map(int,input().strip().split())
arr=[0]*(b-a+1)
for i in range(a,b+1):
    arr2=f(i)
    arr[i-a]=len(arr2)
print(arr.index(max(arr))+a,max(arr))    
