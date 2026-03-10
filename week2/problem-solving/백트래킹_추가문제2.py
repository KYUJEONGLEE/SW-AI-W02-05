# https://www.acmicpc.net/problem/15650

import sys

N, M = sys.stdin.readline().split()


def no_dup_suyeal(n, m):
    result = []
    visited = [False] * n

    def backtracking(start, current_suyeal):

        if len(current_suyeal) == m:
            result_suyeal = current_suyeal.copy()
            result.append(result_suyeal)
            return

        for i in range(start, n):
            if not visited[i]:
                visited[i] = True
                current_suyeal.append(i + 1)
                backtracking(i, current_suyeal)
                visited[i] = False
                current_suyeal.pop()

    backtracking(0, [])
    return result


if __name__ == "__main__":
    output = no_dup_suyeal(int(N), int(M))
    for o in output:
        print(*o)

