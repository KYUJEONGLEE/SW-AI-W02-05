# 1. 그래프 만드는 방법
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

# 2. 그래프 BFS 정석


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            q.append(nxt)
