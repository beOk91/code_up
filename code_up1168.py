jumin1,jumin2=input().strip().split()
if jumin2=="3" or jumin2=="4":
    print(2012-(2000+int(jumin1[:2]))+1)
else:
    print(2012-(1900+int(jumin1[:2]))+1)
