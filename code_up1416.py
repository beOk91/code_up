num=int(input())
arr=[]
if num==0:
    arr.append(0)
while num!=0:
    arr.insert(0,num%2)
    num=num//2 
for element in arr:
    print(element,end="")