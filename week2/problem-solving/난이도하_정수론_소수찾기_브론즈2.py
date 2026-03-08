# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 소수 찾기 알고리즘

# 1과 자기 자신말고 나누어 떨어지는 수가 있는지?

# 1) 2부터 n-1까지 전부 나누어 보는 방법
# 2) 제곱근 확인법


def is_pow(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = n**(0.5)
    for i in range(2, int(sqrt_n) + 1):
        if n % i == 0:
            return False

    return True


def check_pow(input):
    count = 0
    for val in input:
        if is_pow(val):
            count += 1
    print(count)


check_pow(arr)
