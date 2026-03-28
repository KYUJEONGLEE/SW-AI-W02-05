# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
total_coin = 0

for _ in range(N):
    coin = int(sys.stdin.readline())
    coins.append(coin)

coins.reverse()

for coin in coins:
    if K == 0:
        break

    if K // coin != 0:
        total_coin += K // coin
        K -= (K // coin) * coin

print(total_coin)
