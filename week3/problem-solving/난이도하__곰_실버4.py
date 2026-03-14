# 문제 링크: https://www.acmicpc.net/problem/10828
import sys

N = int(sys.stdin.readline())
X = [sys.stdin.readline().rstrip().split() for _ in range(N)]

stack = []
for cmd in X:
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if not stack:
            print("-1")
        else:
            remove_val = stack.pop()
            print(remove_val)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if stack:
            print("0")
        else:
            print("1")
    else:
        if not stack:
            print("-1")
        else:
            print(stack[-1])
