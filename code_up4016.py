num1,num2,num3=map(int,input().strip().split())
for i in range(min(num1,num2,num3),0,-1):
    if num1%i==0 and num2%i==0 and num3%i==0:
        print(i)
        break