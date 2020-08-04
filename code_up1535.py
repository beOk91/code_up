def f(num_list):
    maxIndex=0
    for i in range(len(num_list)):
        if num_list[maxIndex]<num_list[i]:
            maxIndex=i
    return maxIndex+1
num=int(input())
num_list=list(map(int,input().strip().split()))
print(f(num_list))