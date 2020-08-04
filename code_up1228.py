import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
h,w=map(float,input().strip().split())
s_w=(h-100)*0.9
pig_degree=(w-s_w)*100/s_w
if pig_degree<=10:
    print("정상")
elif pig_degree<=20:
    print("과체중")
else:
    print("비만")