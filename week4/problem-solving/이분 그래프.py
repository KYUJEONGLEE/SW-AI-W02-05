# 문제 링크 : https://www.acmicpc.net/problem/1707
"""
그래프의 정점의 집합을 둘로 분할하여
각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때,
이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

순환이 있으면 이분 그래프가 될 수 없다?
짝수개의 간선으로 순환이 된다면 이분그래프가 가능하다. 홀수개면 이분 그래프 불가능
dfs로 뻗어나가면서 각 정점을 색칠한다. 번갈아가면서 다른 색으로 칠하는데
만약 칠하려고 보니 같은 색이면 순환그래프가 아니다?
"""
import sys
sys.setrecursionlimit(10 ** 6)
T = int(sys.stdin.readline())
for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    # visited = [False] * (V + 1)
    color = ["white"] * (V + 1)
    is_inj = False

    for i in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, cur_color):
        global is_inj

        if is_inj:
            return

        color[node] = cur_color
        if cur_color == "Red":
            next_color = "Blue"
        elif cur_color == "Blue":
            next_color = "Red"

        for next in graph[node]:
            if color[next] == "white":
                dfs(next, next_color)
            elif color[next] == cur_color:
                print("NO")
                is_inj = True

            if is_inj:
                break

    for u in range(1, V + 1):
        if color[u] == "white":
            dfs(u, "Red")

    if not is_inj:
        print("YES")
