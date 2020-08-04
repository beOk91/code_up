num=int(input())
sum1=0
for i in range(1,num+1):
    sum2=0
    for j in range(1,i+1):
        sum1+=j
    sum1+=sum2
print(sum1)

