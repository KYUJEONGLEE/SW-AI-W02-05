
# 문제 링크: https://www.acmicpc.net/problem/23309
import sys

N, M = map(int, sys.stdin.buffer.readline().split())
rail = list(map(int, sys.stdin.buffer.readline().split()))
# command = [list(sys.stdin.readline().rstrip().split()) for _ in range(M)]

prev = [0] * 1000001
next = [0] * 1000001
command_line = []

# 입력받은 rail 리스트를 prev, next 의 정보를 담고있는 dictionary 로 가공하는 과정
for index, num in enumerate(rail):
    if index == 0:
        prev[num] = rail[-1]
        next[num] = rail[1]

    elif index == len(rail) - 1:
        prev[num] = rail[index - 1]
        next[num] = rail[0]

    else:
        prev[num] = rail[index - 1]
        next[num] = rail[index + 1]

# 위 과정을 거치면 초기 입력값들이 prev, next에 각각의 다음역, 이전역의 정보를 담고 있는
# dictionary 로 변환된다.
# 백준 입력을 예시로 들면
# next = {2: 7, 7: 3, 3: 5, 5: 2}, prev = {2: 5, 7: 2, 3: 7, 5: 3}

# 이제 입력받은 커맨드들을 하나씩 처리한다.
for _ in range(M):
    cmd = sys.stdin.buffer.readline().split()
    op = cmd[0]

    if op == "BN":
        i = int(cmd[1])
        j = int(cmd[2])

        command_line.append(next[i])
        temp_rail = next[i]

        next[i] = j
        prev[temp_rail] = j
        next[j] = temp_rail
        prev[j] = i

    elif op == "BP":
        i = int(cmd[1])
        j = int(cmd[2])

        command_line.append(prev[i])
        temp_rail = prev[i]

        prev[i] = j
        next[temp_rail] = j
        prev[j] = temp_rail
        next[j] = i

    elif op == "CN":
        i = int(cmd[1])

        command_line.append(next[i])
        temp_rail = next[i]

        next[i] = next[temp_rail]
        prev[next[temp_rail]] = i

    elif op == "CP":
        i = int(cmd[1])

        command_line.append(prev[i])
        temp_rail = prev[i]

        prev[i] = prev[temp_rail]
        next[prev[temp_rail]] = i

print('\n'.join(map(str, command_line)))
