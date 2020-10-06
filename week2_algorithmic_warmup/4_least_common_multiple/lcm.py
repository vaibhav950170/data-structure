# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a,b):
	q=b
	w=a
	while(b!=0):
	    c=a%b
	    a=b
	    b=c

	d=int(w/a)
	r=int(q/a)
	return a*d*r

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

