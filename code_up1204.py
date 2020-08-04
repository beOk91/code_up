num=input()
if num=="11" or num=="12" or num=="13":
    print(num+"th")
else:
    if num[len(num)-1]=="1":
        print(num+"st")
    elif num[len(num)-1]=="2":
        print(num+"nd")
    elif num[len(num)-1]=="3":
        print(num+"rd")
    else:
        print(num+"th")