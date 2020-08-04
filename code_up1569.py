def f(num_list,val):
    for i in range(len(num_list)):
        if num_list[i]==val:
            return i+1
    return -1

num=input()
num_list=list(map(int,input().split()))
val=int(input())
print(f(num_list,val))