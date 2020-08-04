num=int(input())
n_list=list(map(int,input().strip().split()))
arr=[]
for i in range(0,num,2):
    print((n_list[i] if n_list[i]<n_list[i+1] else n_list[i+1]),end=" ")
