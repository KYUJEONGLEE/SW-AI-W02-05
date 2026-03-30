# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    rank = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        rank.append((x, y))

    rank.sort(key=lambda x: x[0])   # 서류 순위 기준 정렬

    count = 1                       # 서류 1등은 무조건 합격
    min_interview = rank[0][1]      # 현재까지 면접 최고 순위(작을수록 좋음)

    for i in range(1, N):
        if rank[i][1] < min_interview:
            count += 1
            min_interview = rank[i][1]

    print(count)
