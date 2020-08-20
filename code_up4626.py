num=int(input())
num_list = list(map(int,input().strip().split()))
num_list2=[]
idx=0
while idx!=num:
    if num_list[idx]==0:
        num_list2.append(0)
    else:
        if idx==0:
            num_list2.append(1)
        else:
            num_list2.append(num_list2[idx-1]+1)
    idx+=1
print(sum(num_list2))