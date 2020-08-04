n=int(input())
n_list=list(map(int,input().strip().split()))
m=int(input())
m_list=list(map(int,input().strip().split()))

common_list=list(element for element in n_list if element in m_list)

n_list.extend(m_list)
sum_list=list(set(n_list))
sum_list.sort()

if len(common_list)==0:
    print(0)
else:
    for element in common_list:
        print(element,end=" ")
    print()
for element in sum_list:
    print(element,end=" ")