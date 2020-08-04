num=int(input())
star=""
for i in range(num):
    star+="*"
    
for i in range(1,10):
    for j in range(i):
        print(star,end="")
    print()