num=int(input())
person_list=[[0 for i in range(3)] for i in range(4)]
for i in range(num):
    num1,num2,num3=map(int,input().strip().split())
    person_list[0][0]+=num1
    person_list[0][num1]+=1
    person_list[1][0]+=num2
    person_list[0][num2]+=1
    person_list[2][0]+=num3
    person_list[0][num3]+=1

winner=0
for i in range(1,3):
    if person_list[winner]<=person_list[i]:
        if person_list[winner]==person_list[i]:
            print(0,person_list[winner])
            winner=-1
            break
        else:
            winner=i
if winner!=-1:
    print(winner+1,person_list[winner])
    13  10 13