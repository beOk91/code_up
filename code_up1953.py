def f(num1,num2):
    if num1<=num2:
        print("*"*num1)
        f(num1+1,num2)

num=int(input())
f(1,num)