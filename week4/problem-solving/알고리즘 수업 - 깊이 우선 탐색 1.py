import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())

edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

visited = list([0] * (N + 1))
count = 1


def create_graph(vertices, edges):
    graph = [[] for i in range(vertices + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for adj_list in graph:
        adj_list.sort()

    return graph


def dfs(V, E, R):
    global count
    visited[R] = count
    for x in E[R]:
        if visited[x] == 0:
            count += 1
            dfs(V, E, x)


if __name__ == "__main__":
    graph = create_graph(N, edges)
    dfs(N, graph, R)
    for _ in range(1, N + 1):
        print(visited[_])
