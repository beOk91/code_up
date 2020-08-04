num=int(input())
cnt=0
for i in range(1,num):
    for j in range(i,num-i):
        k=num-i-j
        if k<i+j and k>=i and k>=j:
            cnt+=1
print(cnt)
