n,k=map(int,input().strip().split()) 
arr=[[" "]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1: 
            arr[i][j]="*"
    
    for j in range(k-1,n*2,k):
        if j-i>=0 and j-i<n and i<n and i>=0:
            arr[i][j-i]="*"
    
for i in range(n):
    for j in range(n):
        print(arr[i][j],end="")
    print()

"""
            (0,2)  (0,5) (0,8)
            (1,1)  (1,4) (1,7)
                   (2,3) (2,6) 
                   (3,2) (3,5) (3,8)
                   (4,1) (4,4) ()
                   (5,0) (5,3)
                         (6,2)
                         (7,1)
                         (8,0)
"""