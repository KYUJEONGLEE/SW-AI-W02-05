# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
"""
n가지 종류의 동전이 있다.
이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
그러면서 동전의 개수가 최소가 되도록 하려고 한다.
각각의 동전은 몇 개라도 사용할 수 있다.
"""
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coin = []

visited = [False] * 10001
dist = [0] * 10001
count = 0

for _ in range(n):
    x = int(sys.stdin.readline())
    coin.append(x)


def bfs(start, end):
    global count
    q = deque([start])
    visited[start] = True
    dist[start] = 0

    while q:
        cur_q = q.popleft()
        count = dist[cur_q]
        count += 1
        if cur_q == end:
            break

        for j in coin:
            sum = cur_q + j
            if not visited[sum] and sum <= k:
                visited[sum] = True
                q.append(sum)
                dist[sum] = count


visited = [False] * 10001

bfs(0, k)
print(dist[k])
