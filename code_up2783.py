s,n=map(int,input().strip().split())
arr=[""]*n
arr2=[0]*n
for i in range(n):
    arr[i]=input()
for i in range(n-(s-1)):
    arr2[i]=sum(1 for element in arr[i:i+s] if element=="Ballad" )
if max(arr2)==0:
    print(0)
else:
    print(arr2.index(max(arr2))+1)