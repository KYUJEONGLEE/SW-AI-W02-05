
# 문제 링크: https://www.acmicpc.net/problem/3190
"""
---------------------------------------------------
처음 떠올린 생각:

게임이 종료되는 순간은 벽에 부딪히거나
본인의 몸과 부딪히거나 게임이 끝난다.

2차원 배열에 뱀이 현재 있는 칸을 1로 표현한다.
그래서 만약 진행하고자 하는 칸이 1이면 종료한다. 
라는 조건을 달아주면 될거같다.

반복문은 while 로 검사해서 충돌 조건(bool)로 빠져나오는건가
큐?

- vector? (1,0)(0,1)(-1,0)(0,-1)
---------------------------------------------------
해결한 방법:

뱀의 몸 전체를 deque로 관리했다.
deque의 앞쪽은 꼬리, 뒤쪽은 머리라고 생각했다.

매 초마다 현재 방향으로 머리를 한 칸 이동시킨다.
이동한 좌표가 이미 deque 안에 있으면 자기 몸과 충돌한 것이고,
보드 범위를 벗어나면 벽에 부딪힌 것이므로 게임을 종료한다.

충돌이 아니라면 새로운 머리 좌표를 deque의 뒤에 추가한다.
이후 해당 칸에 사과가 있는지 확인한다.

사과가 있으면 꼬리를 그대로 두어서 뱀의 길이를 1 늘린다.
사과가 없으면 deque의 앞쪽 원소를 제거해서
길이는 유지한 채 앞으로 한 칸 이동한 상태를 만든다.

방향 전환 명령은 입력된 시간이 지난 직후에 적용한다.
따라서 명령에 적힌 시간까지 먼저 이동한 뒤,
D면 오른쪽 회전, L이면 왼쪽 회전을 하도록 구현했다.

모든 방향 전환 명령을 처리한 뒤에도 게임은 끝나지 않는다.
마지막 명령 이후에는 현재 방향으로 계속 이동하다가
벽이나 자기 몸에 부딪히는 순간 게임을 종료한다.

1. 머리 이동
2. 충돌 검사
3. 머리 추가
4. 사과 여부에 따라 꼬리 유지 또는 제거
5. 방향 전환
을 순서대로 수행하는 시뮬레이션 문제로 해결했다.
---------------------------------------------------
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
