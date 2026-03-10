# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

import sys

N = int(sys.stdin.readline())


def Tower(n, x, y):
    # 함수 기능부터 정의
    # 원반 n 개를 x 에서 y로 옮길떄 이동한 횟수를 반환하는 함수.

    # 1) n - 1 개를 시작 기둥에서 목표가 아닌 기둥으로 옮긴다.(보조기둥)
    # 2) n 을 목표 기둥으로(count + 1)
    # 3) n - 1 개를 보조 기둥에서 목표기둥 으로 옮긴다.

    if n == 1:

        print(f"{x} {y}")
        return

    if n > 1:
        Tower(n - 1, x, 6 - x - y)
        # 시작 기둥 x, 보조 기둥 y, 1) 에서 y는 목표기둥이 아닌 보조기둥
        # 기둥 번호의 합 6, 나머지 기둥의 번호는 6에서 두개를 뺴면 된다.

    print(f"{x} {y}")

    if n > 1:
        Tower(n - 1, 6 - x - y, y)
        # 보조 기둥에서 목표 기둥으로 이동


if __name__ == "__main__":
    print(2**N-1)
    if N <= 20:
        Tower(N, 1, 3)
