num_list=list(map(int,input().strip().split()))
for i in range(10):
    if num_list[i]%5==0:
        print(num_list[i])
        break
    elif i==9 and num_list[i]%5!=0:
        print(0)

        