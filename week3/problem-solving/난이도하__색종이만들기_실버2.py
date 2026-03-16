
# 문제 링크: https://www.acmicpc.net/problem/2630
"""
접근 방법:

큰 문제를 작은 문제로 해결 가능할까 => 재귀?
영역이 같이 않으면 4등분 으로 쪼갠다 -> 더이상 쪼개지지 않을때까지 OR 영역이 같을 때까지 반복
"조건" 이 맞지 않으면 작은 단위로 쪼갠다.
"조건"? => 
1) 영역의 첫 원소 arr[0][0] 과 마지막 원소 arr[i][j] 가 같으면 같은 영역일까? => X
2) row 를 탐색하면서 기준삼은 영억(0 or 1)과 다른 값이 나오면 다른 영역 일까? => X 
ex) 1 1 1 1
    0 1 0 1
    1 0 0 0
    1 1 1 1
3) 그럼 완전탐색하는 방법밖에 없나?
4) 재귀 함수의 인자를 시작점으로 해서 영역의 모든값을 탐색한다.
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_1, cnt_0 = 0, 0


def recursion(row, col, size):
    global cnt_0, cnt_1
    pivot = arr[row][col]
    for i in range(row, size + row):
        for j in range(col, size + col):
            if arr[i][j] != pivot:
                recursion(row, col, size // 2)
                recursion(row, col + size // 2, size // 2)
                recursion(row + size // 2, col, size // 2)
                recursion(row + size // 2, col + size // 2, size // 2)
                return

    if pivot == 0:
        cnt_0 += 1
    else:
        cnt_1 += 1


if __name__ == "__main__":
    recursion(0, 0, N)
    print(f"{cnt_0}\n{cnt_1}")
