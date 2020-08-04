board_y,board_x=map(int,input().strip().split())
tile_y,tile_x=map(int,input().strip().split())
x_tile,spot_tile="",""
tile_list=[]
board=[[""] *board_x for i in range(board_y)]
idx=0
for i in range(tile_y):
    for j in range(tile_x):
        x_tile+="X"
    if i!=(tile_y-1):
        x_tile+="\n"
    
for i in range(tile_y):
    for j in range(tile_x):
        spot_tile+="."
    if i!=(tile_y-1):
        spot_tile+="\n"
tile_list.append(x_tile)
tile_list.append(spot_tile)
print(tile_list)
for i in range(board_y):
    for j in range(board_x):
        board[i][j]=tile_list[idx%2]
        idx+=1

for i in range(board_y):
    for j in range(board_x):
        print(board[i][j],end="")
    print()