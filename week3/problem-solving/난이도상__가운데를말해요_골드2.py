
# 문제 링크: https://www.acmicpc.net/problem/1655
"""
백준 1655
---------------
처음 떠올린 생각:

입력 데이터가 들어올때마다, 실시간으로 데이터들의 대소관계를 비교해서
갱신을 해줘야 할까?

제한시간이 0.1초
입력개수는 100,000개 => nlogn? n?

입력값이 들어올떄마다 sort() 시키면 시간복잡도는 어떻게 될까?

---------------
해결한 방법:

---------------
해결 못한 점:

"""
import sys
from collections import deque

N = int(sys.stdin.readline())
X = []

for _ in range(N):
    x = int(sys.stdin.readline())
    X.append(x)
    X.sort()

    if len(X) % 2 == 0:
        print(X[(len(X) // 2) - 1])
    else:
        print(X[(len(X) // 2)])
