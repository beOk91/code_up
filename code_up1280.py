a,b=map(int,input().strip().split())
sum1=0
sum2=""
for i in range(a,b+1):
    if i%2==0:
        sum1-=i
        sum2=sum2+"-"+str(i)
    else:
        sum1+=i
        sum2=sum2+"+"+str(i)
print(sum2+"="+str(sum1))