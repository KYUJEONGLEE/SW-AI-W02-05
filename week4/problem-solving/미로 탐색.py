# 문제 링크 : https://www.acmicpc.net/problem/2178

"""
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고,
0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때,
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때
지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다.
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
visited = [[False] * (M) for _ in range(N)]
dist = [[0] * (M) for _ in range(N)]
count = 1

for _ in range(N):
    row = list(map(int, sys.stdin.readline().strip()))
    # 입력값이 붙어서 들어올때는 strip() 함수를 사용하면 된다.
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    global count
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    dist[sx][sy] = count

    while q:
        x, y = q.popleft()
        count = dist[x][y]
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            dist[nx][ny] = count
            q.append((nx, ny))

            if nx == N - 1 and ny == M - 1:
                break

    return dist[N-1][M-1]


dist = bfs(0, 0)
print(dist)
