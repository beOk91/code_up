num=int(input())
cnt=0
for i in range(1,num//3+1):
    for j in range(i,num//2+1):
        k=num-i-j
        if k<i+j and k>=i and k>=j:
            print(i,j,k)
            cnt+=1
print(cnt)