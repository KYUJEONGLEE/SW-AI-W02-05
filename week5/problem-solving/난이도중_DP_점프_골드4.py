# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys

N, M = map(int, sys.stdin.readline().split())

x_stone = []

for _ in range(M):
    m = int(sys.stdin.readline())
    x_stone.append(m)
