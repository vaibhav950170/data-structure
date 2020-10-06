# Uses python3
import sys

def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


def fib_period_length(m):
    previous = 0
    current = 1
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_fast(n, m):
    remainder = n % fib_period_length(m)
    return get_fibonacci(remainder) % m


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current


def fibonacci_partial_sum_fast(from_, to):
    if from_ == to:
        return get_fibonacci_last_digit_fast(from_ % 60)
    else:
        from_ %= 60
        to %= 60

        from_last = get_fibonacci_huge_fast(from_ + 1, 10) - 1
        to_last = get_fibonacci_huge_fast(to + 2, 10) - 1

    return (to_last - from_last) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))