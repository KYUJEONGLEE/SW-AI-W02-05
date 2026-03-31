# 문제 링크 : https://www.acmicpc.net/problem/4949

# 소괄호, 대괄호 짝 확인하는 문제 => 스택

import sys

while True:
    pair = True
    sentence = sys.stdin.readline().rstrip()

    if sentence == ".":
        break

    parse = []

    for char in sentence:
        if char == "(":
            parse.append(char)
        elif char == "[":
            parse.append(char)

        if char == ")":
            if not parse or parse[-1] != "(":
                print("no")
                pair = False
                break
            else:
                parse.pop()
        elif char == "]":
            if not parse or parse[-1] != "[":
                print("no")
                pair = False
                break
            else:
                parse.pop()

    if pair and len(parse) == 0:
        print("yes")
    else:
        if pair:
            print("no")
