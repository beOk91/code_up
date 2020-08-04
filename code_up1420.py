num=int(input())
score_list=[]
for i in range(num):
    name,score=input().strip().split()
    score_list.append((name,int(score)))

score_list.sort(key=lambda x:x[1],reverse=True)
print(score_list[2][0])