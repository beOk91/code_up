num=int(input())
num_list=[[0 for i in range(num)] for i in range(num)]
number=1
for i in range(num):
    for j in range(num-1,-1,-1):
        num_list[i][j]=number
        number+=1

for i in range(num):
    for j in range(num):
        print(num_list[i][j],end=" ")
    print()