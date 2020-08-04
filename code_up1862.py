arr=[0]*101
def f(num):
    if arr[num]!=0:
        return arr[num]
    else:
        if num==1 or num==2:
            return 1
        else:
            arr[num]=f(num-1)+f(num-2)
            return arr[num]%1000000007
num=int(input())
print(f(num))