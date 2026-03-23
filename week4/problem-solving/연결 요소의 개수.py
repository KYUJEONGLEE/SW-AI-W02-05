# 문제 링크 : https://www.acmicpc.net/problem/11724

"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

연결 요소 라는게 순환이 있는 정점들의 요소를 뜻하는것? X
덩어리들의 개수를 세는것
방향없는 그래프 => 무방향 그래프 => 두 개 다 추가해주는거였나..
"""
import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

if M == 0:
    print(N)
    sys.exit()

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
# 인접 리스트를 가진 그래프는 만들어졌다.


def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(next)


for _ in graph:
    for v in _:
        if visited[v]:
            continue
        count += 1
        dfs(v)

print(count + (visited.count(False) - 1))
