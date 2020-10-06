# Uses python3
import sys

def get_fibo_last_digit(n):
    a, b= 0,1
    for i in range(2,n+1):
        c=a+b
        c=c%10
        b, a=c, b
        
    return c


n = int(input())
print(get_fibo_last_digit(n))
