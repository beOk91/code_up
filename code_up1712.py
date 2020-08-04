n1,n2,k=map(int,input().strip().split())
arr=[]
i=0
while True:
    val=n1+ (n2-n1)*i
    if val<=k:
        arr.append(val)
        i+=1
    else:
        break
for element in arr:
    print(element,end=" ")