
# 문제 링크: https://www.acmicpc.net/problem/3190
"""
처음 떠올린 생각:
게임이 종료되는 순간은 벽에 부딪히거나
본인의 몸과 부딪히거나 게임이 끝난다.

2차원 배열에 뱀이 현재 있는 칸을 1로 표현한다.
그래서 만약 진행하고자 하는 칸이 1이면 종료한다. 라는 조건을 달아주면 될거같다.

반복문은 while 로 검사해서 충돌 조건(bool)로 빠져나오는건가
큐?

vector? (1,0)(0,1)(-1,0)(0,-1)
"""
import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apple_location = [tuple(map(int, sys.stdin.readline().split())
                        )for _ in range(K)]
apple_location = dict.fromkeys(apple_location, 1)
L = int(sys.stdin.readline())
Command = [sys.stdin.readline().split() for _ in range(L)]


snake_queue = deque([])
x, y = 1, 1

vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]
game_over = False
face = 0
count = 0

if not snake_queue:
    snake_queue.append((x, y))
# snake가 비어있다면 생성
# 일단 처음에는 무조건 오른쪽으로 이동함.


for cmd in Command:

    second = int(cmd[0]) - count
    direction = cmd[1]

    while second > 0:

        count += 1
        x += vector[face][0]
        y += vector[face][1]

        if (x, y) in snake_queue:
            game_over = True
            break

        if x > N or y > N or x <= 0 or y <= 0:  # 부딪힌다면
            game_over = True
            break

        snake_queue.append((x, y))

        if snake_queue[-1] in apple_location:  # 사과가 있다면
            if apple_location[snake_queue[-1]] == 0:
                snake_queue.popleft()

            apple_location[snake_queue[-1]] = 0

        elif snake_queue[-1] not in apple_location:  # 사과가 없다면
            snake_queue.popleft()

        second -= 1

    if direction == "D":
        face = (face + 1) % 4
    elif direction == "L":
        face = (face - 1) % 4
    if game_over:
        break

# face = 2
# direction = 'L'
# count = 13
# K =4
# L =4
# que = deque([(2, 9), (3, 9), (3, 8), (2, 8), (1, 8)])
# x = 1, y = 8
# game_over = False
while not game_over:
    count += 1

    x += vector[face][0]
    y += vector[face][1]

    if (x, y) in snake_queue:
        game_over = True
        break

    if x > N or y > N or x <= 0 or y <= 0:  # 부딪힌다면
        game_over = True
        break

    snake_queue.append((x, y))

    if snake_queue[-1] in apple_location:  # 사과가 있다면
        if apple_location[snake_queue[-1]] == 0:
            snake_queue.popleft()

        apple_location[snake_queue[-1]] = 0

    elif snake_queue[-1] not in apple_location:  # 사과가 없다면
        snake_queue.popleft()

print(count)
