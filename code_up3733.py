import sys
sys.setrecursionlimit(100000)
arr2=[0]*100000
def f(num):
    if arr[num]!=0:
        return arr[num]
    else:
        cnt=1
        orinum=num
        while num!=1:
            cnt+=1
            if num%2==1:
                num=3*num+1
            elif num%2==0:
                num=num//2
        arr[orinum]=cnt
        return cnt
a,b=map(int,input().strip().split())
arr=[0]*(b+1)

for i in range(a,b+1):
    arr[i]=f(i)
print(arr.index(max(arr)),max(arr))