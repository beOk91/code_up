num=int(input())
num_list=map(int,input().split())
sum=0
for element in num_list:
    if element%5==0:
        sum+=element
print(sum)