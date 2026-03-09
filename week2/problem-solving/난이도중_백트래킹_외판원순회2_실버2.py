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
# result = []
distance_cost = []


def TSP(t, move, sum_):
    # move 배열의 경로가 다 정해지면 => 길이가 N이 되면
    # 결과 리스트에 추가해서 경로를 담기
    # 해당 재귀 종료하기?
    final_sum = 0

    if len(move) == len(t):
        # move_route = move.copy()
        # result.append(move_route)
        zero_distance = t[move[-1]][move[0]]
        if zero_distance != 0:
            final_sum = sum_ + t[move[-1]][move[0]]
            distance_cost.append(final_sum)
        return

    for city_num in range(len(t)):
        # 모든 경로의 조합을 찾아보자
        if city_num in move:
            continue
        # 도시를 하나씩 성공적으로 붙이면 경로 가중치 계산
        is_zero_distance = t[move[-1]][city_num]
        if is_zero_distance != 0:
            # sum_ += t[move[-1]][city_num]
            move.append(city_num)
            TSP(t, move, sum_ + t[move[-2]][city_num])
        # // 여기에 pop 호출
        # 여기에서 비용 계산을 진행
        # sum_ -= t[move[-1]][city_num]
            move.pop()

    return distance_cost

    # 여기까지 진행하면 0부터 시작해서 n 까지 도시를 시작점으로 하는 모든 조합의 수가 도출된다.
    # 하지만 문제에서 시작도시는 고정되어 있지 않기 때문에 예를들어
    # 1 -> 3 -> 2 -> 4 의 경로는 2 -> 4 -> 1 -> 3 의 경로와 같다고 판단할 수 있다.
    # 그러면 여기에서 마지막 원소를 i 로 첫번째 원소를 j 로 두고 W[i][j] 의 값(=비용) 을 더해주면
    # 비용을 계산할 수 있다.

    # 3 일떄 시작점이 0인 경로는 2개
    # 4 일때 시작점이 0인 경로는 6개
    # 5 일때 4! = 24개 ... n 일때 (n-1)!
    # 즉 result의 크기가 (n-1)! 이면 그대로 종료해도 괜찮은가?
    # => 간단하게 move의 첫 원소에 0을 넣어주면 0 을 시작점으로 하는 조합들이 만들어진다 :<

    # 경로를 구했으니 비용을 구해보자.
    # 하나의 경로를 완성할떄마다 가중치를 더해서 다른 리스트에 저장하면?
    # 아니면 move에 올바른 경로를 추가할떄마다 비용을 더하는 방법이 있을까?

    # 시간초과


print(min(TSP(T, [0], 0)))

# # 입력 및 초기화
# N = int(sys.stdin.readline())
# T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# distance_cost = []


# def TSP(t, move, sum_):
#     final_sum = 0

#     # 종료 조건: 모든 도시를 방문했을 때
#     if len(move) == len(t):
#         zero_distance = t[move[-1]][move[0]]
#         if zero_distance != 0:
#             final_sum = sum_ + zero_distance
#             distance_cost.append(final_sum)
#         return

#     for city_num in range(len(t)):
#         # 이미 방문한 도시 건너뛰기
#         if city_num in move:
#             continue

#         # 이동 가능한 경로인지 확인 (비용이 0이 아님)
#         is_zero_distance = t[move[-1]][city_num]
#         if is_zero_distance != 0:
#             move.append(city_num)
#             # 재귀 호출: 다음 도시로 이동
#             TSP(t, move, sum_ + is_zero_distance)
#             # 백트래킹: 상태 복구 (pop)
#             move.pop()

#     return distance_cost


# # 0번 도시를 시작점으로 설정하여 호출
# result = TSP(T, [0], 0)
# print(min(result))
