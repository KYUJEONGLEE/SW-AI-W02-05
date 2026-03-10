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
        if len(current_combination) == n:
            count += 1
            return
        # row 는 backtracking의 인자로 들어간다
        # row번째 행에 퀸을 어느 열에 놓을까?
        for col in range(n):

            # 퀸을 놓을 수 있는지 검사
            # 검사해야 할 항목
            # 1. 같은 열인지 (같은 행인지 검사는 한 행에 하나만 놓기로 설정하므로 필요없다.)
            # 2. 대각선에 위치하는지
            if col in current_combination:
                continue

            is_diagonal = False
            # current 에 담긴 정보를 바탕으로 prev 를 얻어올 수있다.
            for prev_row, prev_col in enumerate(current_combination):
                if abs(row - prev_row) == abs(col - prev_col):
                    is_diagonal = True
                    break

            if not is_diagonal:
                # 현재 놓으려는 위치 (row, col)
                # 이전의 위치를 어떻게 받아올까?
                # current_combination 의 리스트값으로 가져올수있다.
                # 현재 row = 3 라고 했을때, 예를 들어 current에는 [0, 3, 5] 가 들어있다고 하자
                # 전에 놓인 퀸의 위치는 2행 5열 이다. 즉 row - 1 행과 current의 마지막 열[-1]
                # 어차피 바로 전의 행이랑 비교하므로 열 인덱스끼리의 차이가 1 이면 대각선이지 않을까?
                # => 안됐다
                current_combination.append(col)
                # current_combination 에는 각 행에 놓인 퀸의 열 번호가 들어간다
                backtracking(row + 1, current_combination)
                # 행을 하나씩 증가시킨다.
                current_combination.pop()

    backtracking(0, [])
    return count


if __name__ == "__main__":
    s = Queen(N)
    print(s)
