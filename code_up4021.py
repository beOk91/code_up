num_list=list(map(int,input().strip().split()))
sum=0
for i in range(7):
    if num_list[i]%2==1:
        sum+=num_list[i]
if sum==0:
    sum=-1
print(sum)