# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    d = [0] * (M + 1)

    d[0] = 1

    for coin in coins:
        for i in range(1, M + 1):
            if i - coin < 0:
                continue
            d[i] = d[i] + d[i - coin]

    print(d[M])
