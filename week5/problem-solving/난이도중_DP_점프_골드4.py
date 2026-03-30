# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys

N, M = map(int, sys.stdin.readline().split())
stone = set()
for _ in range(M):
    m = int(sys.stdin.readline())
    stone.add(m)

dp = [[float("inf")] * (int((2 * N) ** 0.5) + 3) for _ in range(N + 1)]

dp[1][0] = 0

for i in range(2, N + 1):
    if i in stone:
        continue

    for jump in range(1, (int((2 * N) ** 0.5) + 2) + 1):
        if i - jump < 1:
            continue

        result = []

        if jump - 1 >= 0:
            result.append(dp[i - jump][jump - 1])
        result.append(dp[i - jump][jump])
        if jump + 1 <= (int((2 * N) ** 0.5) + 2):
            result.append(dp[i - jump][jump + 1])

        best = min(result) + 1
        dp[i][jump] = best

answer = min(dp[N])

if answer == float("inf"):
    print("-1")
else:
    print(answer)
