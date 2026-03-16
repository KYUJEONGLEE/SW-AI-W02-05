
# 문제 링크: https://www.acmicpc.net/problem/2493

N = int(input())
Tower = list(map(int, input().split()))

compare_stack = []
answer = [0] * N
stack_count = 0

# for tower in Tower[::-1]:
#     compare_stack.append(tower)
#     Tower.pop()

#     for tower2 in Tower[::-1]:
#         if not compare_stack:
#             break

#         if tower2 > tower:
#             while compare_stack:
#                 compare_stack.pop()
#                 answer.append(stack_count)
#         else:
#             Tower.pop()
#             compare_stack.append(tower2)
origin_tower = len(Tower)
while Tower:
    # 입력 Tower 리스트가 존재하면
    # 비교스택이 비어있으면 새로 원소 추가
    if not compare_stack:
        compare_stack.append((len(Tower), Tower[-1]))
        Tower.pop()
    # 비교스택이 비어있지 않으면, 즉 비교해야 하는 상황이 있으면
    else:
        if compare_stack[-1][1] > Tower[-1]:
            compare_stack.append((len(Tower), Tower[-1]))
            Tower.pop()
        else:
            while compare_stack and compare_stack[-1][1] < Tower[-1]:
                answer[compare_stack[-1][0] - 1] = len(Tower)
                compare_stack.pop()

print(*answer, end='')
