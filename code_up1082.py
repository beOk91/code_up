num = input()
num_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
if num >='A' and num<='F':
    num = int(num_list[ord(num)-55])
for i in range(1,16):
    print("%X*%X=%X" %(num,i,num*i))