# 이진 검색

def binary_search(key, array):
    # key = 찾고자 하는 값, array = 배열
    pl, pr = 0, len(array) - 1

    # pl,pr,pc 를 설정
    # 각 의미는 배열의 왼쪽값, 오른쪽값, 중앙값

    # key 값과 array[pc] 을 비교한다
    # key = array[pc] 이면 pc 값을 반환하고 종료한다.

    # key < array[pc] 인 경우, 배열 왼쪽에 key가 존재할수밖에 없으므로
    # 왼쪽 범위로 배열을 좁힌다.
    # pl은 그대로, pr은 pc - 1 로 바꾼다. pc의 값도 다시 재할당

    # key > array[pc] 인 경우, 배열 오른쪽에 key가 존재하므로
    # 오른쪽 범위로 배열을 좁힌다.
    # pl은 pc + 1, pr은 그대로. pc의 값도 다시 재할당

    # 만약 pr > pl 일 경우, key 는 배열에 존재하지 않는다.

    # 반복문의 구조를 어떻게 짜야할까?

    while True:
        pc = (pl + pr) // 2
        # pc는 로직이 반복될때마다 공통적으로 재할당하는 변수
        # 그러므로 while 문이 시작할때 재할당 시킨다.

        # 위 pl > pr 조건문을 어디다가 놓아야 연산을 덜 할까?
        # 굳이 반복문을 한번 더 들어갈 필요없이 마지막에서 종료조건을 검사해주면
        # 연산 횟수가 1번 줄어든다.
        if array[pc] == key:
            return pc
        elif array[pc] > key:
            pr = pc - 1
        elif array[pc] < key:
            pl = pc + 1

        if pl > pr:
            return -1
        # 탐색 종료 조건을 반복문 끝에서 검사


if __name__ == "__main__":
    test_array = [2, 6, 9, 11, 15, 16, 19, 21, 26]
    n = 21
    is_key_in_array = binary_search(n, test_array)
    print(is_key_in_array)
