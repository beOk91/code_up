sum=0    
num_list=[]
for i in range(4):
    getOff,getOn=map(int,input().strip().split())
    sum+=getOn
    sum-=getOff
    num_list.append(sum)
print(max(num_list))