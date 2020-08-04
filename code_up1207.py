num_list=list(map(int,input().strip().split()))
cnt=0
for i in range(4):
    if num_list[i]==1:
        cnt+=1
if cnt==1:
    print("도")
elif cnt==2:
    print("개")
elif cnt==3:
    print("걸")
elif cnt==4:
    print("윷")
else:
    print("모")