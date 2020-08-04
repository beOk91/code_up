board=[[] for i in range(10)]
for i in range(10):
    board[i]=input().split(" ")

chk=False
i=1
j=1

while True:
    if chk==True or i==9:
        break 
    if board[i][j]=="2":
        chk=True
        board[i][j]=9
    elif board[i][j]=="1":
        j-=1
        i+=1
        continue
    else:
        board[i][j]=9
        j+=1 

for i in range(10):
    for j in range(10):
        print(board[i][j],end=" ")
    print()