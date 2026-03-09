# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
# 최댓값을 출력한다.

# 순서를 바꿔서 나올 수 있는 값
# 원소의 최대 개수가 8 이므로 나올 수 있는 모든 순서조합으로 최댓값을 찾는다.
# 나올 수 있는 조합의 개수 8!

# 이것도 백트래킹으로 풀수 있지 않을까?
#


def perm(n):
    length_n = len(n)
    result = []

    def backtracking(current_perm, visited, sum_of_val):
        # 종료 조건 : 현재의 조합의 길이가 n의 길이와 같은 경우
        if len(current_perm) == length_n:
            result_perm = current_perm.copy()
            result.append(result_perm)
            return

        for i in range(length_n):
            # current_combination 에 넣는 조건 => 사용하지 않은 원소일때
            if not visited[i]:
                visited[i] = True
                current_perm.append(n[i])
                backtracking(current_perm, visited, sum_of_val)
                current_perm.pop()
                visited[i] = False

    backtracking([], [False] * length_n, 0)
    print(result)
    # 순열들의 리스트를 만드는 것 부터 구현했음.


if __name__ == "__main__":
    perm(X)
