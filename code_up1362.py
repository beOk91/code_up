n=int(input())
sum1=0
for i in range(1,n+1):
    sum1+=i
for i in range(n):
    for j in range(i+1):
        print(sum1,end=" ")
        sum1-=1
    print()