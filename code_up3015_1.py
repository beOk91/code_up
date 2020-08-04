class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        self.__score=score

num1,num2=map(int,input().split())
arr=[]
for i in range(num1):
    info1,info2=input().split()
    arr.append(Student(info1,int(info2)))

arr.sort(key=lambda x: x.score,reverse=True)

for i in range(num2):
    print(arr[i].name)