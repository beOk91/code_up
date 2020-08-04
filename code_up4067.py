n,m=map(int,input().strip().split())
arr=[[0]*n for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))

score_info=[]
for i in range(n):
    score_info.append(arr[i][0]*3+arr[i][1])
rank=sorted(score_info,reverse=True)
print(rank.index(score_info[m-1])+1)