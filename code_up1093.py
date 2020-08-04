cnt=int(input())
list_a=input().split(" ")
list_b=[]
for i in range(23):
    list_b.append(0)
for i in range(cnt):
    list_b[int(list_a[i])-1]+=1
for i in range(23):
    print(list_b[i], end=" ")