# 문제 링크: https://www.acmicpc.net/problem/1697
"""
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때,
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

최단 시간 BFS?
이게 어떻게 BFS지

5 17
5 - 10 - 9 - 18 - 17 = 4초

"""

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False] * 100001
dist = [0] * 100001
count = 0
# N은 시작 정점
# K는 도착 정점
# 각 노드들은 N + 1, N -1, 2 * N 의 인접 리스트를 가진다.
# 인저 노드들을 하나씩 방문하면서 K에 도착하는 최소 시간(거리)

# 현재 위치를 꺼내면 즉석에서 만든다. 라는 생각을 가질 수 있어야 한다.


def bfs(start, end):
    global count
    q = deque([start])
    visited[start] = True
    dist[start] = 0

    while q:
        cur_q = q.popleft()
        count = dist[cur_q]

        if cur_q == end:
            break

        count += 1
        sub_q = cur_q - 1
        plus_q = cur_q + 1
        double_q = 2 * cur_q

        if sub_q >= 0 and not visited[sub_q]:
            visited[sub_q] = True
            q.append(sub_q)
            dist[sub_q] = count
        if plus_q <= 100000 and not visited[plus_q]:
            visited[plus_q] = True
            q.append(plus_q)
            dist[plus_q] = count
        if double_q <= 100000 and not visited[double_q]:
            visited[double_q] = True
            q.append(double_q)
            dist[double_q] = count


bfs(N, K)
