num=int(input())
rest=0
for i in range(num):
    cnt,apple=map(int,input().split())
    rest+=apple%cnt
print(rest)