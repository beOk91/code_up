num=int(input())
num_list1=list(map(int,input().strip().split()))
num_list2=sorted(num_list1,reverse=True)
for element in num_list1:
    print(element, num_list2.index(element)+1)