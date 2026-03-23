# 문제 링크 : https://www.acmicpc.net/problem/10026
"""
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N * N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

R R R B B
G G B B B
B B B R R
B B R R R
R R R R R

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다.
(빨강 2, 파랑 1, 초록 1) 하지만,
적록색약인 사람은 구역을 3개 볼 수 있다.(빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때,
적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

N = int(sys.stdin.readline())
count = 0
RG_count = 0
graph = []
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    row = list(sys.stdin.readline().strip())
    graph.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if graph[x][y] == graph[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        count += 1
        bfs(i, j)


visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'


for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        RG_count += 1
        bfs(i, j)

print(f"{count} {RG_count}")
