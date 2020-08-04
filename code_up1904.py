def f(num1,num2):
    if num1<=num2:
        if num1%2==1:
            print(num1,end=" ")
        f(num1+1,num2)

num1,num2 = map(int,input().split())
f(num1,num2)