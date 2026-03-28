# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys
from collections import deque
exp = sys.stdin.readline().rstrip()

op_stack = []
operand_stack = deque()
temp = ""

for operator in exp:
    if operator == '+' or operator == '-':
        op_stack.append(operator)
        temp = int(temp)
        operand_stack.append(temp)
        temp = ""
    else:
        temp += operator

temp = int(temp)
operand_stack.append(temp)

# 문자열 파싱 완료

"""
분배법칙까지 생각해야한다.
첫 - 가 등장하면 뒤의 값을 다 괄호로 묶어준다.
왜냐하면 연산의 값이 최소가 되려면 - 값 이후의 값이 제일 큰 값이여야 하기 때문이다.
- 다음에 나오는 덩어리 안의 연산자에 대해서 생각 할 필요가 없다.
뒤에 나오는 + 들은 괄호로 묶어주면 영향을 - 분배의 영향을 받지 않기 때문이다.
예를 들어 55 + 50 - 40 - 30 + 80 - 90 이 입력값으로 주어졌을때
55 + 50 - (40 - 30 + 80 - 90) 으로 묶어준다.
결국에는 55 + 50 - (40 + (30 + 80) + 90) 이 된다.
"""
sub_index = 0
for idx, val in enumerate(op_stack):
    if val == '-':
        sub_index = idx
        break
    else:
        sub_index = -1

plus_val = 0
prefix = 0

copy_stack = operand_stack.copy()

for idx, operand in enumerate(copy_stack):
    plus_val += operand
    operand_stack.popleft()

    if sub_index == -1:
        while operand_stack:
            plus_val += operand_stack.popleft()
        break

    if idx == sub_index:
        while operand_stack:
            prefix += operand_stack.popleft()
        break


print(plus_val - prefix)
