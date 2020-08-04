import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
year,month,day=input().split(" ")
if int((int(year)+int(month)+int(day))/100)%10%2==0:
    print("대박")
else:
    print("그럭저럭")
    