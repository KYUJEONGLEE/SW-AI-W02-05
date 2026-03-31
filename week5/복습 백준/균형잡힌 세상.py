# 문제 링크 : https://www.acmicpc.net/problem/4949

# 소괄호, 대괄호 짝 확인하는 문제 => 스택

import sys

while True:
    sentence = sys.stdin.readline().rstrip()

    if sentence == ".":
        break

    small = []
    big = []

    for char in sentence:
        if char == "(":
            small.append(char)
        elif char == "[":
            big.append(char)
        elif char == ")":
            small.pop()
        elif char == "]":
            big.pop()

    if len(small) == 0 and len(big) == 0:
        print("yes")
    else:
        print("no")
