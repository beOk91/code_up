a,b=map(int,input().strip().split())
a_list=list(map(int,input().strip().split()))
b_list=list(map(int,input().strip().split()))
a_list.extend(b_list)
a_list.sort()
for element in a_list:
    print(element,end=" ")   