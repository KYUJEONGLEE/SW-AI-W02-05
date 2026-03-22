# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
"""
문제 접근 방법:
1번 컴퓨터와 연결 되어 있지 않은 컴퓨터를 걸러내는 작업이 필요
=> 연결 되어 있는 컴퓨터만 COUNT 하는 문제
1) 일단 주어진 vertices와 edges로 그래프를 만든다(dictionary)
2) root 을 queue 에 넣고, visited [] 에 append
3) queue 가 빌때까지 반복문
4) q = queue 원소 pop -> 그래프의 q 정점에 있는 모든 정점들을
    visited[] 에 없다면 q에 추가
5) visited[] 에 추가할때 count + 1

왜 틀릴까..

해결 방법:
방향그래프로 그래프를 생성했었다 => 무방향 그래프로 바꿔줌
ex) (2, 1) 로 연결이 표시되어 있으면 탐색을 못했음

"""
from collections import deque
import sys
sys.exit()

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
edge = list(tuple(map(int, sys.stdin.readline().split()))
            for _ in range(E))


def create_graph(vertices, edges):
    graph = {i: [] for i in range(1, vertices + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def virus(graph, root):
    visited = []
    count = 0
    q = deque()

    # 첫 루트 q에 삽입, visited 삽입
    q.append(root)
    visited.append(root)

    while q:
        cur_q = q.popleft()
        for e in graph[cur_q]:
            if e not in visited:
                q.append(e)
                visited.append(e)
                count += 1

    return count


if __name__ == "__main__":
    graph = create_graph(V, edge)
    virus_computer = virus(graph, 1)
    print(virus_computer)
