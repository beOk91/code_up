n=int(input())
k=list(map(int,input().strip().split()))
for i in range(n):
    for j in range(n):
        print(k[j],end=" ")
    print()
    k.append(k.pop(0))