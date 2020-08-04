num=int(input())
num_list=list(map(int,input().strip().split()))
for i in range(num):
    print("{}:".format(i+1),end=" ")
    for j in range(num):
        if i!=j:
            if num_list[i]<num_list[j]:
                print("<",end=" ")
            elif num_list[i]==num_list[j]:
                print("=",end=" ")
            else:
                print(">",end=" ")
    print()
