num_list=list(map(int,input().strip().split()))
num_list.sort()
if num_list[2]<(num_list[0]+num_list[1]):
    print("yes")
else:
    print("no")