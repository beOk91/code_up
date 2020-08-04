num=int(input())
arr=[]
arr2=[]
for i in range(num):
    game=input()
    if game in arr:
        arr2[arr.index(game)]+=1
    else:
        arr.append(game)
        arr2.append(1)

for i in range(len(arr)):
    print(str(i+1)+" "+arr[i]+" : "+str(arr2[i]))