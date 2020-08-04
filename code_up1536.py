def f(num_list):
    num_list2=[]
    for element in num_list:
        num_list2.append(int(element))
    return min(num_list2)

num=int(input())
num_list=input().split()
print(f(num_list))