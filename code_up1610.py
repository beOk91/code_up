def f(str_list,num_range):
    range1,range2=map(int,num_range.split())
    return str_list[range1:range1+range2]
str_list=input().strip()
num_range=input().strip()
print(f(str_list,num_range))