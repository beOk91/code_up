num=int(input())
num_list=list(map(int,input().strip().split()))
find_num=int(input())
if find_num not in num_list:
    print(-1)
else:
    print(num_list.index(find_num)+1)