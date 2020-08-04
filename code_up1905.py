"""
import sys
sys.setrecursionlimit(30000)
"""
def f(num1):
    if num1==1:
        return 1
    return num1+f(num1-1)

num=int(input())
print(f(num))