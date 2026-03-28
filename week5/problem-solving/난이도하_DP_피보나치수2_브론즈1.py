# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())


def fibo(n, memo=None):
    if memo is None:
        memo = {}

    memo[0] = 0
    memo[1] = 1

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)

    return memo[n]


result = fibo(n-1)
print(result)
