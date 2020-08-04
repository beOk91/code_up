num=list(input())
result=sum(int(num[i]) for i in range(len(num)))%7
if result==4:
    print("Bad")
else:
    print("Good")