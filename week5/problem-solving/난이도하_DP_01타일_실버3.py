# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

import sys
sys.setrecursionlimit(10 ** 8)
N = int(sys.stdin.readline())


def tile(n, d=None):

    if d is None:
        d = {}

    d[0] = 1
    d[1] = 2

    if n <= 1:
        return n + 1

    if n in d:
        return d[n]

    for i in range(2, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 15746

    return d[n]


print(tile(N - 1))
