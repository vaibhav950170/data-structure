# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    
    n=(n+2)%60

    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current%10, (previous + current)%10
    if current == 0:
        return 9
    else:
        return current-1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
