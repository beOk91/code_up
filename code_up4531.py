num_list=[]
sum=0
for i in range(5):
    num_list.append(int(input()))
    sum+=num_list[i]
num_list.sort()
print(int(sum/5))
print(num_list[2])