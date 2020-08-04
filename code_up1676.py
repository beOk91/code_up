num=int(input())
num_list1=list(map(int,input().strip().split()))
num_list2=num_list1.copy()
num_list2.sort(reverse=True)
for element in num_list1:
    print(num_list2.index(element)+1)
