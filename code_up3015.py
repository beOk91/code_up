class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        self.__score=score
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

arr=[]
num1,num2=map(int,input().split())
for i in range(num1):
    info1,info2=input().split()
    arr.append(Student(info1,int(info2)))

for i in range(num1):
    for j in range(num1-i-1):
        if arr[j].score<arr[j+1].score:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp

for i in range(num2):
    print(arr[i].name)