a,b=map(int,input().strip().split())
n_list=[a+b,a-b,a*b]
n_list.sort()
print(n_list[1])