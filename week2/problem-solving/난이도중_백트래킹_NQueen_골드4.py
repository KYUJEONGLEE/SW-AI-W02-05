# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

import sys

N = int(sys.stdin.readline())

# 크기가 N * N 인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제

# 1) 기본 베이스 생각 => 한 행에는 Q 한개만 놓을 수 있다.
# 같은 행과 같은 열은 백트래킹으로 들어가지 않는다.
# 대각선 판단이 되면 역시 백트래킹으로 들어가지 않는다.


def Queen(n):

    count = 0

    def backtracking(row, current_combination):
        nonlocal count
        # 단순하게 조건을 모두 충족하는 조합이 있다면 count를 증가시키면 된다.
        if len(current_combination) == n:
            nonlocal count
            count += 1
            return
        # row 는 backtracking의 인자로 들어간다
        # row번째 행에 퀸을 어느 열에 놓을까?
        for col in range(n):
            # 퀸을 놓을 수 있는지 검사

    backtracking(0, [])
    return count


if __name__ == "__main__":
    s = Queen(N)
