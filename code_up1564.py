def f(num1,num2):
    for i in range(min(num1,num2),1,-1):
        if num1%i==0 and num2%i==0:
            return i
    return 1
num1,num2=map(int,input().strip().split())
print(f(num1,num2))