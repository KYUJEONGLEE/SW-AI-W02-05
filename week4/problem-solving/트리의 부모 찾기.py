# 뮨제 링크 : https://www.acmicpc.net/problem/11725

"""
루트 없는 트리가 주어진다.
이때, 트리의 루트를 1이라고 정했을 때,
각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

"""
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
answer = [0] * (N - 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(node):
    q = deque([node])
    visited[node] = True

    while q:
        cur_q = q.popleft()

        for next in graph[cur_q]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                answer[next - 2] = cur_q


bfs(1)
print(*answer, sep='\n')
