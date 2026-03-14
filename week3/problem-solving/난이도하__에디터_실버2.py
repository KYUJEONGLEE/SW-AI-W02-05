
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys

initial_text = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
command_line = [sys.stdin.readline().split() for _ in range(N)]


def command(initial_text_buffer, command_box):
    # 핵심 아이디어 : 커서를 기준으로 왼쪽, 오른쪽 스택을 2개 만든다.
    # 커서의 위치를 바꾸지말고, 커서가 이동할때마다 양쪽의 스택의 상태를 바꾼다.
    left_stack = list(initial_text_buffer)
    # 굳이 list 로 다시 바꿔줄 필요가없고 입력할때 리스트로 받자
    right_stack = []

    for command in command_box:
        if command[0] == 'L':
            if left_stack:
                shift_to_R = left_stack.pop()
                right_stack.append(shift_to_R)
        elif command[0] == 'D':
            if right_stack:
                shift_to_L = right_stack.pop()
                left_stack.append(shift_to_L)
        elif command[0] == 'B':
            if left_stack:
                left_stack.pop()
        elif command[0] == 'P':
            left_stack.append(command[1])

    right_stack.reverse()
    return left_stack + right_stack


if __name__ == "__main__":
    result = command(initial_text, command_line)
    print(''.join(result))
