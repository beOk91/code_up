cnt=int(input())
white_stone_list=[[] for i in range(cnt)]

for i in range(cnt):
    white_stone_list[i]=input().split(" ")

board=[[0 for i in range(19)] for j in range(19)]

for i in range(cnt):
    board[int(white_stone_list[i][0])-1][int(white_stone_list[i][1])-1]=1

for i in range(19):
    for j in range(19):
        print(board[i][j], end=" ")
    print()
