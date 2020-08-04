import sys
def quicksort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr)//2]
  left=[x for x in arr if x<pivot]
  mid = [x for x in arr if x == pivot]
  right = [x for x in arr if x>pivot]
  return quicksort(right) + mid +quicksort(left)
def f(arr,i,j,k):
    arr2=list(arr[i-1:j])
    arr2.sort(reverse=True)
    degree=arr2[k-1]
    val=sum(1 for i in arr2 if i==degree)
    print(degree,val)  
n,m=map(int,sys.stdin.readline().strip().split())
arr=list(map(int,sys.stdin.readline().strip().split()))
for _ in range(m):
    i,j,k=map(int,sys.stdin.readline().strip().split())
    f(arr,i,j,k)