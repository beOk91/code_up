import sys
num_list=list(map(int,sys.stdin.readline().strip().split()))
print((num_list[i] for i in range(len(num_list)) if (i+1)%50==0),end=" ")