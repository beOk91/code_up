n=int(input())
sum=1
for i in range(2,n+1):
    i=str(i)
    if len(i)>=2 and i[len(i)-1]=="1":
        sum+=1
print(sum)