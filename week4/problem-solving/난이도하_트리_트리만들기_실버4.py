# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
import sys

N, M = sys.stdin.readline().split()
N, M = int(N), int(M)

# N 개의 정점, M개의 리프노드(차수가 1인 = 본인한테 연결되어 있는 간선의 수가 1)

for i in range(N - 1):
    if i < N - M + 1:
        print(f"{i} {i + 1}")
    else:
        print(f"{N - M} {i + 1}")
