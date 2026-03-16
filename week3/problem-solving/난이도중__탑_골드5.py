N = int(input())
Tower = list(map(int, input().split()))

compare_stack = []
answer = [0] * N

origin_tower = len(Tower)
while Tower:
    if not compare_stack:
        compare_stack.append((len(Tower), Tower[-1]))
        Tower.pop()
    else:
        if compare_stack[-1][1] > Tower[-1]:
            compare_stack.append((len(Tower), Tower[-1]))
            Tower.pop()
        else:
            while compare_stack and compare_stack[-1][1] < Tower[-1]:
                answer[compare_stack[-1][0] - 1] = len(Tower)
                compare_stack.pop()

print(*answer, end='')
