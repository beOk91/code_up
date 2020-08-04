t_list=list(map(int,input().strip().split()))
cnt=0
for element in t_list:
    if element<=170:
        print("CRASH {}".format(element))
        break
    else:
        cnt+=1
if cnt==3:
    print("PASS")