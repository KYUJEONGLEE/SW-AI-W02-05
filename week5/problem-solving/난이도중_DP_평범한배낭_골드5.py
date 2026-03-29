# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys

N, K = map(int, sys.stdin.readline().split())
bag = []
dp = [[0] * (K + 1) for _ in range(N+1)]
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    bag.append((W, V))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if bag[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-bag[i-1][0]] + bag[i-1][1], dp[i-1][j])

print(dp[N][K])
