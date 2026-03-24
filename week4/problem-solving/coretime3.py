from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        graph = [list(map(int, row)) for row in grid]
        # 문자열 지도를 숫자 지도로 바꿔줌

        visited = [[False] * len(graph[0]) for _ in range(len(graph))]
        # 방문 배열 선언

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        # 상하좌우 이동을 위한 장치

        def bfs(sx, sy):
            # 해당 좌표의 상하좌우를 돌면서 검사
            q = deque([(sx, sy)])
            visited[sx][sy] = True
            # 방문 체크
            while q:
                x, y = q.popleft()

                for i in range(4):
                    # 상하좌우 이동 로직
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 격자판을 벗어나지않는 조건 + 방문했거나 + 0(바다) 인 경우 다음 상하좌우로 이동
                    if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                        continue
                    if visited[nx][ny]:
                        continue
                    if graph[nx][ny] == 0:
                        continue

                    # 위 조건들을 다 통과했다면
                    # 즉, 1. 보드판 안에 있고
                    #     2. 방문 안했고
                    #     3. 섬이다.

                    # 방문처리 + q 삽입
                    visited[nx][ny] = True
                    q.append((nx, ny))

        count = 0
        # 섬 개수 count 변수

        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == 1 and not visited[i][j]:
                    # 전체 graph 를 돌면서 위 조건
                    # 1. 섬인데
                    # 2. 아직 방문 안한
                    # 만족한다면 bfs 호출
                    # count + 1
                    bfs(i, j)
                    count += 1

        return count
