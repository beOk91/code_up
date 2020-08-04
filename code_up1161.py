val1,val2=(input().rstrip()).split(" ")
if int(val1)%2==0:
    print("짝수",end="")
else:
    print("홀수",end="")
print("+",end="")
if int(val2)%2==0:
    print("짝수",end="")
else:
    print("홀수",end="")
print("=",end="")
if (int(val1)%2==0 and int(val2)%2==0) or (int(val1)%2!=0 and int(val2)%2!=0):
    print("짝수",end="")
else:
    print("홀수",end="")