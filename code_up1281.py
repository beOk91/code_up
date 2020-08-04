a,b=map(int,input().strip().split())
result1=""
result2=0
for i in range(a,b+1):
    if i%2==0:
        result1=result1+"-"+str(i)
        result2-=i
    else:
        if i==a:
            result1=str(i)
            result2=i
        else:
            result1=result1+"+"+str(i)
            result2+=i
print(result1+"="+str(result2))