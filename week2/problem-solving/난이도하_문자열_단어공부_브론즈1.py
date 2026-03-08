# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

import sys

S = sys.stdin.readline().rstrip()


def count_word(input):
    count_alpha = 0
    max_list = []
    input = input.upper()
    # 1. count() 함수로 () 안에 있는 요소가 몇번 나오는지 체크
    # cf) 'A'를 아스키코드로 변환하면 65 , chr(숫자) => 문자로 변환, ord(문자) => 숫자
    # 2. max_list = 알파벳 숫자만큼(26) 각 문자가 나온 횟수가 기록된 리스트
    for i in range(26):
        count_alpha = input.count(chr(i + 65))
        max_list.append(count_alpha)
    # 최댓값을 저장
    max_val = max(max_list)
    max_index = max_list.index(max_val)

    if max_list.count(max_val) > 1:
        print("?")
    else:
        print(chr(max_index + 65))


count_word(S)
