# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    rank = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        rank.append((x, y))
