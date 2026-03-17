# 문제 링크: https://www.acmicpc.net/problem/1629
"""
---------------
처음 떠올린 생각:

 A, B, C는 모두 2,147,483,647 이하의 자연수?
 그럼 최대 값은 2,147,483,647 ^ 2,147,483,647 ?
 그냥 제곱 ** 써서 나머지 연산 하면 되는것 아닌가? => 시간초과 나는구나
 반복문이 없어도 연산하는 값이 크면 시간초과가 난다.

 그럼 시간복잡도를 줄이는 방법
 이걸 어떻게 나눌까?
---------------
해결한 방법:
모듈러 분배 법칙
(A + B) mod C = {(A mod C) + (B mod C)} mod C 이다.

---------------

"""
import sys
X, Y, Z = map(int, sys.stdin.readline().split())


def recursion(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        temp = recursion(a, b // 2, c)
        return ((temp % c) * (temp % c)) % c
    else:
        temp = recursion(a, b // 2, c)
        return ((temp % c) * (temp % c) * (a % c)) % c


print(recursion(X, Y, Z))
