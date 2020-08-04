def f(num_list):
    num_list.sort()
    return num_list[1]
num_list=list(map(int,input().strip().split()))
print(f(num_list))