def f(num_list,index_list):
    sum=0
    for i in range(index_list[0]-1,index_list[1]):
        sum+=num_list[i]
    return sum
num=int(input())
num_list=list(map(int,input().strip().split()))
index_list=list(map(int,input().strip().split()))
print(f(num_list,index_list))