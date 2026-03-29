# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline())

room_time = []
using = []
count = 0
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    room_time.append((start, end))

# 끝나는 시간 기준으로 작은 수부터 정렬
# 끝나는 시간이 같다면 시작 시간이 작은 순으로 정렬


def reservation_room(check):
    global count
    check.sort(key=lambda x: (x[1], x[0]))

    using.append(check[0])
    count += 1

    for start, end in check[1:]:
        if start >= using[-1][1]:
            using.append((start, end))
            count += 1

    return count


print(reservation_room(room_time))
