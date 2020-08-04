a,b=map(int,input().strip().split())
sum1=0
for i in range(a,b+1):
    for j in range(len(str(i))):
        if str(i)[j]=="1":
            sum1+=1
print(sum1)