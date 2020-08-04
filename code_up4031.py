num_list=list(map(int,input().strip().split()))
even,odd=0,0
for i in range(len(num_list)):
    if num_list[i]%2==0:
        if even<num_list[i]:
            even=num_list[i]
    else:
        if odd<num_list[i]:
            odd=num_list[i]
print(even+odd)