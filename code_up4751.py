num=int(input())
arr,cnt=[],0
country=[0]*101
for i in range(num):
    countryNum,no,score=map(int,input().strip().split())
    arr.append([countryNum,no,score])
arr.sort(key=lambda x:x[2],reverse=True)
for i in range(num):
    if cnt==3:
        break
    if country[arr[i][0]]!=2:
        print(arr[i][0],arr[i][1])
        country[arr[i][0]]+=1
        cnt+=1