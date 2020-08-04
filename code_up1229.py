h,w=input().split()
h=float(h)
w=float(w)
standard_w,degree=0,0
if h<150:
    standard_w=h-100
elif h<160:
    standard_w=(h-150)/2+50
else:
    standard_w=(h-100)*0.9
degree=(w-standard_w)*100/standard_w
if degree<=10:
    print("정상")
elif degree<=20:
    print("과체중")
else:
    print("비만")