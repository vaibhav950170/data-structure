# Uses python3
import sys

def get_change(m):
    sum=0
    while(m>=10):
        sum+=1
        m-=10
    while(m>=5):
        sum+=1
        m-=5
    while(m>=1):
        sum+=1
        m-=1
    return sum

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
