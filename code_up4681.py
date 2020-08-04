num_list=input().strip().split()
sum=0
for i in range(5):
    sum+=int(num_list[i])*int(num_list[i])
print(sum%10)