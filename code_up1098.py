h,w=input().split(" ")
board=[[0 for i in range(int(w))] for j in range(int(h))]
n=int(input())
for i in range(n):
    bar=input().split(" ")
    if bar[1]=="0":
        for j in range(int(bar[3])-1,int(bar[3])-1+int(bar[0])):
            if j>=int(w):
                break
            else:
                board[int(bar[2])-1][j]=1
    else:
        for j in range(int(bar[2])-1,int(bar[2])-1+int(bar[0])):
            if j>=int(h):
                break
            else:
                board[j][int(bar[3])-1]=1
for i in range(int(h)):
    for j in range(int(w)):
        print(board[i][j],end=" ") 
    print()