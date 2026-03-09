# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

import sys
N = int(sys.stdin.readline())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 0 10 15 20
# 5 0 9 10
# 6 13 0 12
# 8 8 9 0

# 위 배열에서 생각해보자.
# 모든 도시를 방문해서 거리 비용이 최소값인 조합을 찾아라
# 예시에서 N = 4, 종료조건은 비용 리스트의 길이가 4가 됬을때
# len(cost_list) == N
# 비용조합 리스트에 추가

# 방문했던 도시를 판단할 수 있는 방법은?
result = []


def TSP(t, start_city, move):
    # move 배열의 경로가 다 정해지면 => 길이가 N이 되면
    # 결과 리스트에 추가해서 경로를 담기
    # 해당 재귀 종료하기?
    if len(move) == len(t):
        move_route = move.copy()
        result.append(move_route)
        return

    for city_num in range(len(t)):
        # 모든 경로의 조합을 찾아보자
        if city_num in move:
            continue
        move.append(city_num)
        TSP(t, start_city, move)
        # // 여기에 pop 호출
        move.pop()
    print(result)


TSP(T, 0, [])
