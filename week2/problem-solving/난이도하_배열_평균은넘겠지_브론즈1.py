# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

import sys

C = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(C)]


def calc_AVG_rate(input):
    for class_id in input:
        student_count = class_id[0]
        # sum_of_score = 0
        above_avg_count = 0

        sum_of_score = sum(class_id[1:])
        # sum 함수 사용법
        # 리스트 인덱싱과 동일 => index 1부터 끝까지 더하려면 list[1:]

        # for i in range(1, len(class_id)):
        #     sum_of_score += class_id[i]

        avg_score = sum_of_score / student_count

        for i in range(1, len(class_id)):
            if class_id[i] > avg_score:
                above_avg_count += 1

        above_average_ratio = round(above_avg_count / student_count * 100, 3)
        print(f"{above_average_ratio}%")


calc_AVG_rate(arr)
