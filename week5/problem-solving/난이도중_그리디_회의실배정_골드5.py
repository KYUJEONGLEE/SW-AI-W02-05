# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline())

room_time = []
count = 0
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    room_time.append((start, end))

# 끝나는 시간 기준으로 작은 수부터 정렬


def reservation_room(check):
    check.sort(key=lambda x: x[1])
    for start, end in check:
        print("")


reservation_room(room_time)
