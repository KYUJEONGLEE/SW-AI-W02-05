# 문제 링크: https://www.acmicpc.net/problem/2164

import sys
from collections import deque

N = int(sys.stdin.readline())

# N 의 범위가 <= 500,000 으로 넓게 제시되어 있다.
# 왼쪽 원소를 마지막에 붙이고, 왼쪽 원소를 버리는 과정이 반복되므로
# 큐를 사용한다.


def queue_Card(n: int) -> deque:
    Card = deque()
    for i in range(1, n+1):
        Card.append(i)

    return Card


def Card_2(card_arr: deque) -> int:
    while len(card_arr) > 1:
        card_arr.popleft()
        lift_card = card_arr.popleft()
        card_arr.append(lift_card)

    return card_arr[0]


if __name__ == "__main__":
    card = queue_Card(N)
    final_card = Card_2(card)
    print(final_card)
