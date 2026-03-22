# 문제 링크 : https://www.acmicpc.net/problem/1012

import sys
from collections import deque

T = int(sys.stdin.readline())
"""
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
그 배추들 역시 해충으로부터 보호받을 수 있다. 
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 
배추들이최소 5마리의 배추흰지렁이가 필요하다. 
0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
예를 들어 배추밭이 아래와 같이 구성되어 있으면 져 있는 땅을 나타낸다.

[1, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 1, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 1, 1, 1, 0]

"""

"""
문재 해결 방법:
인접 해 있는 1들의 묶음을 센다.
1들의 덩어리

DFS/BFS 문제 풀떄, 공식적인 템플릿이 있다.
이건 2차원 배열이므로 해당 뼈대를 사용할 수 있을까?
"""


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    count = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        board[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if __name__ == "__main__":
        for i in range(M):
            for j in range(N):
                if board[i][j] == 1 and visited[i][j] is False:
                    count += 1
                    bfs(i, j)

        print(count)
