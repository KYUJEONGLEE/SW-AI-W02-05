def seq_search(n, list):
    # n이 제시 되었을때, 주어진 배열에서 n값이 존재하면 True 없으면 False 를 반환하는 함수.

    # 순서대로 정렬되지 않은 배열에서 탐색이므로 인덱스 0부터 배열끝까지 탐색한다.
    # 반복문 조건 => i = 0 부터 끝까지(배열의 마지막 인덱스 = 배열 길이 - 1)
    # 헷갈릴만한 부분 -> range는 마지막 숫자를 포함하지 않는다.

    for i in range(len(list)):
        # 만약 list의 i번째 값이 n이라면 인덱스 i와, True를 반환한다.
        if list[i] == n:
            return i, True

    # 반복문을 통해 배열을 끝까지 탐색했음에도 찾지 못한다면
    # 반복문을 빠져나와서 False 를 반환한다.
    return False


if __name__ == "__main__":
    N = 12345
    array = [3, 23, 21, 65, 3, 2314, 21, 3, 23, 123,
             5, 31, 5, 15, 5, 23, 23, 12, 23, 2, 3, 12345]
    is_n_in_array = seq_search(N, array)
    print(is_n_in_array)

    # return 받는 변수는 하나인데 i, True 로 받아도 오류가 안나고 튜플?로 반환받는다
    # 파이썬은 동적인 언어라서 자동으로
