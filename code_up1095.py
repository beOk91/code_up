cnt=int(input())
list_a=input().split(" ")
for i in range(len(list_a)):
    if list_a[i]!='':
        list_a[i]=int(list_a[i])
    else:
        list_a.remove('')
print(min(list_a))