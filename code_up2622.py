num=int(input())
num_list=list(map(int,input().split()))
print("{} : {}".format(num_list.index(max(num_list))+1,max(num_list)))
print("{} : {}".format(num_list.index(min(num_list))+1,min(num_list)))