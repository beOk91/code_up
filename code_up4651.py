for i in range(3):
    num_list=list(map(int,input().strip().split()))
    cnt=0
    for j in range(len(num_list)):
        if num_list[j]==1:
            cnt+=1
    if cnt==1:
        print("C")
    elif cnt==2:
        print("B")
    elif cnt==3:
        print("A")
    elif cnt==4:
        print("E")
    else:
        print("D")