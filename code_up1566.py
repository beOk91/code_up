num1,num2=map(int,input().strip().split())
result=1
if num1==1:
    print(1)
elif num2==0:
    print(1)
else:
    for i in range(num2):
        result*=num1
    print(result)