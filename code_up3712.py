def f(n):
    result=1
    if n%3!=0:
        return 0
    else:
        for i in range(n//3):
            result*=2
        return result%100000007 
num=int(input())
print(f(num))