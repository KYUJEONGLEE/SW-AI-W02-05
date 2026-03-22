# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
"""
문제 접근 방법:
그래프를 만들어서 모든 정점을 순회하는 최소 간선 개수를 구하자

해결 방법:
n - 1
"""
import sys


# def create_graph(vertices, edges):
#     graph = {i: [] for i in range(1, vertices + 1)}
#     for u, v in edges:
#         graph[u].append(v)
#         graph[v].append(u)

#     return graph


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = sys.stdin.readline().split()
        edge = list(tuple(map(int, sys.stdin.readline().split()))
                    for _ in range(int(M)))

        print(int(N)-1)
