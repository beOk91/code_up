class Student:
    def __init__(self,no,name):
        self.no=no
        self.name=name
    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self,no):
        self.__no=no
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

num=int(input())
arr=[]
id_arr=[]
for i in range(num):
    c,no,name=input().strip().split()
    if c=="I":
        if int(no) not in id_arr:
            id_arr.append(int(no))
            arr.append(Student(int(no),name))
        else:
            id_arr.append(int(no))
            arr.insert(0,Student(int(no),name))
    elif c=="D":
        if int(no) in id_arr:
            id_arr.remove(int(no))
            for j in range(len(arr)):
                if arr[j].no==int(no):
                    del arr[j]
                    break
        
print_arr=input().strip().split()
arr.sort(key=lambda x:x.no)
for i in range(len(print_arr)):
    print(arr[int(print_arr[i])-1].no,arr[int(print_arr[i])-1].name)