# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    rank = []
    selected = set()
    count = 1
    N = int(sys.stdin.readline())
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        rank.append((x, y))

    if len(rank) == 1:
        print(len(rank))
    else:
        doc = sorted(rank, key=lambda x: x[0])
        interview = sorted(rank, key=lambda x: x[1])

        min_doc = doc[0]
        min_inter = interview[0]
        # doc = min(rank, key=lambda x: x[0])
        # interview = min(rank, key=lambda x: x[1])

        selected.add(min_doc)
        selected.add(min_inter)

        for a, b in doc:
            if b < min_doc[1]:
                min_doc = (a, b)
                selected.add(min_doc)

        for a, b in interview:
            if (a, b) in selected and a < min_inter[0]:
                min_inter = (a, b)
                count += 1

        print(count)
