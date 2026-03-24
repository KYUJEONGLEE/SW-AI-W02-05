# 문제 링크 : https://www.acmicpc.net/problem/2252
"""
N명의 학생들을 키 순서대로 줄을 세우려고 한다.
각 학생의 키를 직접 재서 정렬하면 간단하겠지만,
마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다.
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때,
줄을 세우는 프로그램을 작성하시오.

A B 이면 학생 A가 학생 B의 앞에 서야 한다는 의미이다?
=> 화살표 방향이 A -> B ?
"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)

"""
진입차수가 0인 정점을 먼저 넣는다.
"""


def line(indegree):
    q = deque()
    # 진입차수가 0인 정점을 찾아야하는데?
    for idx, v in enumerate(indegree):
        if idx == 0:
            continue
        if len(v) == 0:
            q.append([idx])

    # 그럼 q에 진입차수가 0인 정점들이 들어와있다.


line(graph)
