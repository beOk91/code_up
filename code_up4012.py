num=int(input())
score_list=list(map(int,input().split()))
rank_list=sorted(score_list,reverse=True)
for i in range(num):
    print(score_list[i],rank_list.index(score_list[i])+1)