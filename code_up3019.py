num=int(input())
arr=[]
for i in range(num):
    name,year,month,day=input().strip().split()
    arr.append([name,int(year),int(month),int(day)])
arr.sort(key=lambda x: (x[1],x[2],x[3],x[0]))

for element in arr:
    print(element[0])
