# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

"""
문제 접근 방법:
쪨리가 승리할 수 있는지 검사하라
1) 어떻게 그래프를 만들까 -> root 부터 시작해서 각 칸에 적힌 숫자만큼
    무슨 방법으로 간선을 이어주면 될까
2) 값을 검사하는 과정이 필요한가?
3) 결국 시작점에서 끝점까지 경로가 있는가에 대한 문제인거같은데

해결 방법:
그래프를 명시적으로 만들지 않아도 되는 경우가 많다
"""

import sys
from collections import deque

N = int(sys.stdin.readline())
M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

"""
1 1 10
1 5 1   => [ [1 1 10] [1 5 1] [2 2 -1] ]
2 2 -1
"""
visited = [[0] * N for _ in range(N)]
start = (0, 0)
visited[0][0] = 1
find = False

q = deque()
q.append(start)

while q:
    cur_x, cur_y = q.popleft()
    if visited[cur_x][cur_y] == 0:
        visited[cur_x][cur_y] = 1
    is_end = M[cur_x][cur_y]
    if is_end == -1:
        print("HaruHaru")
        find = True
        break
    else:

        if cur_x + is_end < N and visited[cur_x + is_end][cur_y] == 0:
            q.append((cur_x + is_end, cur_y))
        if cur_y + is_end < N and visited[cur_x][cur_y + is_end] == 0:
            q.append((cur_x, cur_y + is_end))


if not find:
    print("Hing")
