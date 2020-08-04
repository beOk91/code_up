num=int(input())
num2=num/2
result=1
for i in range(1,num//2+1):
    if i*(num2-i)>result:
        result=int(i*(num2-i))
print(result)
