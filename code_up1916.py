fibo_list = [0] * 201
def fibonacci(num):
    if fibo_list[num-1]!=0:
        return fibo_list[num-1]
    else:
        if num==1 or num==2:
            fibo_list[0]=1
            fibo_list[1]=1
            return 1
        else:
            fibo_list[num-1]=fibonacci(num-1)+fibonacci(num-2)
            return fibo_list[num-1]

num=int(input())
print(fibonacci(num%10009))