# 문제 링크 : https://www.acmicpc.net/problem/1005

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
D = list(map(int, sys.stdin.readline().split()))

graph = {i: [] for i in range(N + 1)}
indegree = {i: 0 for i in range(N + 1)}
dist = []
order = []

for _ in range(K):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

W = int(sys.stdin.readline())

q = deque()
# 일단 먼저 지어야 하는 건물들의 번호부터 출력해보자
for i in indegree:
    if i == 0:
        continue
    if indegree[i] == 0:
        q.append(i)

while q:
    cur_q = q.popleft()
    order.append(cur_q)

    for next in graph[cur_q]:
        indegree[next] -= 1

        if indegree[next] == 0:
            q.append(next)
