val1,val2,val3,val4=input().split(" ")
result=int(val1)
for i in range(int(val4)-1):
    result=(result*int(val2))+int(val3)

print(result)