# Uses python3
import sys

def gcd_naive(a, b):
    if b==0:
    	return 0
    
    else:
    	while(b!=0):
    		c=a%b
    		a=b
    		b=c
    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
