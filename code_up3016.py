num=int(input())
arr=[]

for i in range(num):
    name,a,b,c=input().strip().split()
    arr.append([name,int(a),int(b),int(c)])

subject1=sorted(arr,key=lambda x:x[1],reverse=True)
subject2=[arr[i][2] for i in range(num)]
subject2.sort(reverse=True)
subject3=[arr[i][3] for i in range(num)]
subject3.sort(reverse=True)

print(subject1[0][0],subject2.index(subject1[0][2])+1,subject3.index(subject1[0][3])+1)