num_list=list(map(int,input().strip().split()))
average=sum(num_list)/10
print("%.1f" %(sum(num_list)/10))
num=0
for element in num_list:
    if average<=element:
        num+=1
print(num,10-num)