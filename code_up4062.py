import math
def m_lcm(arr):
    arr2=arr
    if len(arr)>2:
        a=arr2.pop()
        b=arr2.pop()
        arr2.append(a*b//math.gcd(a,b))
        return m_lcm(arr2)
    else:
        a=arr2.pop()
        b=arr2.pop()
        return a*b//math.gcd(a,b)

def m_gcd(arr):
    arr2=arr.copy()
    if len(arr)>2:
        arr2.append(math.gcd(arr2.pop(),arr2.pop()))
        return m_gcd(arr2)
    else:
        return math.gcd(arr2.pop(),arr2.pop())
n=input()
n_list=list(map(int,input().strip().split()))
print(m_gcd(n_list))
print(m_lcm(n_list))
