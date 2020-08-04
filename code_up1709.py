num=int(input())
num_list=list(map(int,input().strip().split()))
num_list.sort(reverse=True)
for i in range(num):
    print(num_list[i],end=" ")