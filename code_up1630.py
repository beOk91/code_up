import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
num=int(input())
arr=[]
for i in range(num):
    arr.append(input())
for i in range(num):
    print(arr[i])
    if i!=num-1:
        print("AMOLED")