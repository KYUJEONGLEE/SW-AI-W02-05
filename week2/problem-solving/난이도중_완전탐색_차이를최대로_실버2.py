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


def perm(n):
    length_n = len(n)
    max_val = 0

    def backtracking(current_perm, visited, sum_of_val):
        # 종료 조건 : 현재의 조합의 길이가 n의 길이와 같은 경우
        if len(current_perm) == length_n:
            # 순열 리스트 대신 절대값들의 합을 저장함

            # 새로 배운거 nonlocal : 함수 바로 밖에서 선언된 변수에 대해서
            # 안쪽 함수에서 수정 가능하게 할 수 있도록 하는것
            nonlocal max_val

            if max_val < sum_of_val:
                max_val = sum_of_val

            return

        for i in range(length_n):
            # current_combination 에 넣는 조건 => 사용하지 않은 원소일때
            if not visited[i]:
                visited[i] = True
                current_perm.append(n[i])

                # 순열안에 들어있는 원소의 개수가 1개 이하라면 절대값 계산 불가
                if len(current_perm) <= 1:
                    abs_sub = 0

                # 순열안에 2개 이상의 원소가 들어있을때부터 절대값 차이 계산
                elif len(current_perm) > 1:
                    # 끝에서 2개의 원소를 뺼셈
                    abs_sub = abs(current_perm[-1] - current_perm[-2])
                    # 그 값을 sum_of_val에 갱신
                    sum_of_val += abs_sub

                backtracking(current_perm, visited, sum_of_val)
                sum_of_val -= abs_sub
                current_perm.pop()
                visited[i] = False

    backtracking([], [False] * length_n, 0)
    return max_val


if __name__ == "__main__":
    print(perm(X))
