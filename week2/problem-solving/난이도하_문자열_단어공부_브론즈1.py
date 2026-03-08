# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

import sys

S = sys.stdin.readline().rstrip()


def count_word(input):
    input = input.upper()
    # 1. 알파벳 개수만큼의 list 생성
    count_list = [0] * 26
    for s in input:
        # 2. 유니코드로 변환시킨 s 값 - 65 index에 ++
        count_list[ord(s)-65] += 1

    # max_val = 0
    # max_idx = 0
    dup_count = 0
    check_duplicate = False

    # for idx, val in enumerate(count_list):
    #     if val > max_val:
    #         max_val = val
    #         max_idx = idx

    max_val = max(count_list)
    max_idx = count_list.index(max_val)

    for val in count_list:
        if max_val == val:
            dup_count += 1
        if dup_count == 2:
            check_duplicate = True
            break

    if check_duplicate:
        print("?")
    else:
        print(chr(max_idx+65))


count_word(S)
