# 백준 : https://www.acmicpc.net/problem/15649

import sys

N, M = sys.stdin.readline().split()


def suyeal(n, m):
    result = []
    visited = [False] * n

    def backtracking(current_suyeal):

        if len(current_suyeal) == m:
            result_suyeal = current_suyeal.copy()
            result.append(result_suyeal)
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                current_suyeal.append(i + 1)
                backtracking(current_suyeal)
                visited[i] = False
                current_suyeal.pop()

    backtracking([])
    return result


if __name__ == "__main__":
    output = suyeal(int(N), int(M))
    for o in output:
        print(*o)
