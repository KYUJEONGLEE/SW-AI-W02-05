# 문제 링크 : https://www.acmicpc.net/problem/1260
import sys
from collections import deque

"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

간선이 양방향? => 무방향?
"""
N, M, V = map(int, sys.stdin.readline().split())
visited = [False] * (N + 1)
dfs_visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

# print(graph)


def bfs(graph, start):
    q = deque([start])
    visited[start] = True

    while q:
        cur_q = q.popleft()
        print(cur_q, end=' ')
        for v in graph[cur_q]:
            if not visited[v]:
                visited[v] = True
                q.append(v)


def dfs(graph, cur):
    dfs_visited[cur] = True
    print(cur, end=' ')
    for next in graph[cur]:
        if not dfs_visited[next]:
            dfs(graph, next)


dfs(graph, V)
print()
bfs(graph, V)
