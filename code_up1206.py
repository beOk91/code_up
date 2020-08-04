a,b=map(int,input().strip().split())
if a%b==0:
    print("{}*{}={}".format(b,int(a/b),a))
elif b%a==0:
    print("{}*{}={}".format(a,int(b/a),b))
else:
    print("none")