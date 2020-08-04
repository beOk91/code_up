height_list=list(map(int,input().strip().split()))
height_list.sort(reverse=True)
print(height_list[2])