
# 문제 링크: https://www.acmicpc.net/problem/23309
import sys

N, M = map(int, sys.stdin.readline().split())
rail = list(map(int, sys.stdin.readline().split()))
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
    cmd = sys.stdin.readline().split()
    if cmd[0] == "BN":
        cmd[1] = int(cmd[1])
        cmd[2] = int(cmd[2])
        # print(f"{next[cmd[1]]}")
        command_line.append(next[cmd[1]])
        temp_rail = next[cmd[1]]
        # 해당 역의 다음 역을 출력 완료
        # cmd[2]의 역을 cmd[1]의 역 다음으로 설정한다.
        next[cmd[1]] = cmd[2]
        prev[temp_rail] = cmd[2]
        # 그리고 새롭게 추가 된 역의 다음역을 기존 cmd[1] 이 가리키고 있던
        # 역으로 설정한다.
        next[cmd[2]] = temp_rail
        prev[cmd[2]] = cmd[1]
        # 추가적으로 한개의 역을 삽입햇다고 prev도 같이 변경해줘야한다.
    elif cmd[0] == "BP":
        cmd[1] = int(cmd[1])
        cmd[2] = int(cmd[2])

        # print(f"{prev[cmd[1]]}")
        command_line.append(prev[cmd[1]])
        temp_rail = prev[cmd[1]]

        prev[cmd[1]] = cmd[2]
        next[temp_rail] = cmd[2]

        prev[cmd[2]] = temp_rail
        next[cmd[2]] = cmd[1]

    # 삭제하는 연산
    elif cmd[0] == "CN":
        cmd[1] = int(cmd[1])

        # print(f"{next[cmd[1]]}")
        command_line.append(next[cmd[1]])
        temp_rail = next[cmd[1]]

        next[cmd[1]] = next[temp_rail]
        prev[next[temp_rail]] = cmd[1]

        # del next[temp_rail]
        # del prev[temp_rail]

    elif cmd[0] == "CP":
        cmd[1] = int(cmd[1])

        # print(f"{prev[cmd[1]]}")
        command_line.append(prev[cmd[1]])
        temp_rail = prev[cmd[1]]

        prev[cmd[1]] = prev[temp_rail]
        next[prev[temp_rail]] = cmd[1]

        # del next[temp_rail]
        # del prev[temp_rail]

print('\n'.join(map(str, command_line)))
