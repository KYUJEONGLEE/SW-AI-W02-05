# 문제 링크 : https://www.acmicpc.net/problem/10773
import sys

K = int(sys.stdin.readline())
stack = []
for _ in range(K):
    val = int(sys.stdin.readline())
    if val == 0:
        stack.pop()
    else:
        stack.append(val)

print(sum(stack))
