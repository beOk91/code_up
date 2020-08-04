import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
n,confirm_code=input().split()
arr=[[0]*7 for i in range(int(n)) ]
for i in range(int(n)):
    no,name=input().strip().split(",")
    arr[i]=['"'+no+'"','"'+name+'"','"'+confirm_code+'"','"0"','""','"0"','"0"']
for i in range(int(n)):
    print(",".join(arr[i]))