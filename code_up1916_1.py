fibo_list={1:1,2:1}
def fibo(num):
    if num in fibo_list:
        return fibo_list[num]
    else:
        fibo_list[num]=fibo(num-1)+fibo(num-2)
        return fibo_list[num]
num = int(input())
print(fibo(num))