n,k=map(int,input().strip().split())
result=n//k
if result>9999:
    print("번호 초과 오류")
else:
    for i in range(1,result+1):
        print("F-%.4d" %i)