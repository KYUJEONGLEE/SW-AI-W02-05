# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

import sys

T = int(sys.stdin.readline())
S_list = [list(sys.stdin.readline().split()) for _ in range(T)]


def repeat_string(input):
    for S in input:
        repeat_count = int(S[0])
        repeat_str = S[1]

        for s in repeat_str:
            print(s * repeat_count, end="")
        print("")


repeat_string(S_list)
