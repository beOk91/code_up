num=int(input())
arr=[
"*x*",
" xx",
"* *"    
]

for i in range(len(arr)):
    for _ in range(num):
        for j in range(len(arr[i])):
                for _ in range(num):
                    print(arr[i][j],end="")
        print()