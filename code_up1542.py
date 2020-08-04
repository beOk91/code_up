def f(num):
    for i in range(2,num):
        if num%i==0:
            return "composite"
    return "prime"
num=int(input())
print(f(num))