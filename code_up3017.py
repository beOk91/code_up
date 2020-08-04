num=int(input())
number=1
score_list=[]
for i in range(num):
    math,info=map(int,input().split())
    score_list.append([number,math,info])
    number+=1
score_list.sort(key=lambda x:(x[1],x[2],-x[0]), reverse=True)
for element in score_list:
    print(element[0],element[1],element[2])