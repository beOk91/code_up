arr=[[0]*15 for i in range(15)]
def superSum(k,n):
    if arr[k][n]!=0:
        return arr[k][n]
    else:
        if k==0:
            arr[0][n]=n
        else:
            val=0
            for i in range(1,n+1):
                val+=superSum(k-1,i)
            arr[k][n]=val
        return arr[k][n]

while True:
    a,b=map(int,input().strip().split())
    print(superSum(a,b))