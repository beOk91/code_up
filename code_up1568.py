def f(num_list,index_list):
    maxIndex=index_list[0]-1
    for i in range(index_list[0]-1,index_list[1]):
        if(num_list[maxIndex]<num_list[i]):
            maxIndex=i
    return maxIndex+1
num=int(input())
num_list=list(map(int,input().strip().split()))
index_list=list(map(int,input().strip().split()))
print(f(num_list,index_list))