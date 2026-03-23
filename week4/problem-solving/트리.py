# 문제 링크 : https://www.acmicpc.net/problem/1068
"""
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오.
노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

예를 들어, 다음과 같은 트리가 있다고 하자.

     (0)
     / \
   (1) (2)
   / \
 (3)  (4)

현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.

     (0)
     / \
   (x) (2)
   / \
 (x)  (x)


이제 리프 노드의 개수는 1개이다.

입력값이 부모배열이니까 list[i] = p 에서 i 노드의 부모는 p
p의 자식은 i => p의 자식 리스트를 만든다.
"""
import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
R = int(sys.stdin.readline())

child_list = [[] for _ in range(N)]
visited = [False] * N
count = 0

for idx, val in enumerate(P):
    if val == -1:
        root = idx
        continue
    child_list[val].append(idx)


def dfs(node):
    global count

    visited[node] = True
    removed = []
    for next in child_list[node]:
        if next == R:
            continue
        removed.append(next)

    if len(removed) == 0:
        count += 1
        return

    for next in removed:
        dfs(next)


if R == root:
    print(0)
else:
    dfs(root)
    print(count)
