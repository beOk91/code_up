num1,num2=input().split()
num_list=[[0 for i in range(int(num2))] for i in range(int(num1))]
number=1
for i in range(int(num1)-1,-1,-1):
    for j in range(int(num2)-1,-1,-1):
        num_list[i][j]=number
        number+=1

for i in range(int(num1)):
    for j in range(int(num2)):
        print(num_list[i][j],end=" ")
    print()