
# 문제 링크: https://www.acmicpc.net/problem/2470

"""
백준 2470 - 두 용액(골드5)
---------------
처음 떠올린 생각:
알칼리성, 산성 따지지않고 그냥 입력리스트에서 
두 수를 골라 합이 0이 제일 가까운것을 고르는 문제인거같다.
입력 배열 원소의 개수는 100,000개. 원소의 범위는 -1,000,000,000 ~ 1,000,000,000
원소값은 중복은 안된다.

두 수의 합(절댓값)? 을 구해서 스택에 있는 원소와 비교하면서 push?
0과 가까운 숫자라는 걸 어떻게 판단할까 => 절댒값을 사용하면?
입력배열의 크기가 100,000 이므로 n^2 = 10,000,000,000
하나씩 비교는 불가능

sort()?
---------------
해결한 방법:
투 포인터

---------------

"""
import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

start = 0
end = N - 1
min = 100000000

answer = []
X.sort()

while start < end:
    if X[start] + X[end] == 0:
        print(f"{X[start]} {X[end]}")

    if X[start] + X[end] < 0:
        # 값이 음수면 start의 값이 커져야 0에 가까워 진다.
        if min >= abs(X[start] + X[end]):
            min = abs(X[start] + X[end])
            min_x = X[start]
            min_y = X[end]

        start += 1
    else:
        if min >= abs(X[start] + X[end]):
            min = abs(X[start] + X[end])
            min_x = X[start]
            min_y = X[end]
        end -= 1

print(f"{min_x} {min_y}")
