# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

import sys

arr = [int(sys.stdin.readline().strip()) for _ in range(9)]

# 최댓값 로직
# 1. 초기 최댓값 설정 ex) -1
# 2. 리스트 탐색하면서 최댓값 갱신
# 3. 최댓값 반환


def max_value(input_arr):
    max_val, max_idx = 0, 0
    for idx, val in enumerate(input_arr):
        if val > max_val:
            max_val = val
            max_idx = idx

    print(max_val)
    print(max_idx+1)


max_value(arr)
