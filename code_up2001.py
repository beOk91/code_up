pasta1=int(input())
pasta2=int(input())
pasta3=int(input())
juice1=int(input())
juice2=int(input())
price = (min(pasta1,pasta2,pasta3)+min(juice1,juice2))*1.1
print("%.1f" %price)