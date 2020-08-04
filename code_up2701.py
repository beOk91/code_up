myLocation=int(input())
exit_list=list(map(int,input().strip().split()))
closest_exit=max(exit_list)
for element in exit_list:
    if abs(element-myLocation)<closest_exit:
        closest_exit=abs(element-myLocation)
print(closest_exit)