num=int(input())
num_list=map(int,input().split())
cnt=0
for element in num_list:
    if element%2==0:
        cnt+=1
print(cnt)