"""

초기 접근 방법 :
배열의 최대 크기가 100,000개 , 범위는 -2^31 ~ 2^31
M의 배열에서 N에 있는 원소들과 비교해야 하기 때문에 완전탐색으로 찾을 시, 최대 m*n = 100,000,000,00
어떤 탐색을 써야 시간초과가 나지 않을까 생각한다.

set은 membership test(포함 여부 확인) 에 강하다
하지만 순서, 개수, 위치, 경로, 최적값 이 필요하면 단독으로는 부족하다

이 문제는 단순히 존재하느냐 라는 것을 물어보는 문제이므로 set으로 N 배열을 생성한다.

"""
import sys

N = int(sys.stdin.readline())
X = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
Y = list(map(int, sys.stdin.readline().split()))

for y in Y:
    if y in X:
        print("1")
    else:
        print("0")
