array=[[] for i in range(19)]
for i in range(19):
    array[i]=input().split(" ")

cnt=int(input())
for i in range(cnt):
    list_a=input().split(" ")
    for j in range(19):
        if array[int(list_a[0])-1][j]=="0":
            array[int(list_a[0])-1][j]="1"
        else:
            array[int(list_a[0])-1][j]="0"
    for j in range(19):
        if array[j][int(list_a[1])-1]=="0":
            array[j][int(list_a[1])-1]="1"
        else:
            array[j][int(list_a[1])-1]="0"
            
for i in range(19):
    for j in range(19):
        print(array[i][j],end=" ")
    print()