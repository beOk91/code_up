def f(n,k):
    if k==0:
        return n[k]
    else:
        return n[k]+f(n,k-1)
text=input()
print(int(f(text,len(text)-1)))