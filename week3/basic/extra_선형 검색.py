def seq_search(n, list):
    # n이 제시 되었을때, 주어진 배열에서 n값이 존재하면 index, 없으면 -1 를 반환하는 함수.

    # 순서대로 정렬되지 않은 배열에서 탐색이므로 인덱스 0부터 배열끝까지 탐색한다.
    # 반복문 조건 => i = 0 부터 끝까지(배열의 마지막 인덱스 = 배열 길이 - 1)
    # 헷갈릴만한 부분 -> range는 마지막 숫자를 포함하지 않는다.

    for i in range(len(list)):
        # 만약 list의 i번째 값이 n이라면 인덱스 i 를 반환한다.
        if list[i] == n:
            return i

    # 반복문을 통해 배열을 끝까지 탐색했음에도 찾지 못한다면
    # 반복문을 빠져나와서 -1 를 반환한다.
    return -1


def sentinel_seq_search(n, list):
    # n이 제시 되었을때, 주어진 배열에서 n값이 존재하면 True 없으면 False 를 반환하는 함수.
    # 보초법

    copy_list = list.copy()
    copy_list.append(n)

    for i in range(len(copy_list)):
        # copy_list의 i번째 값이 n이고, i가 list의 길이가 아니라면 즉, 마지막 원소가 아니라면
        # i를 반환하고, i가 list의 길이라면(마지막 원소라면) -1 을 반환한다.
        if copy_list[i] == n:
            return i if i != len(list) else -1
        # 주의, 보초법은 복사된 리스트의 길이와 비교하는게 아니라 원래 리스트의 길이와 비교해야한다.


if __name__ == "__main__":
    N = 315
    array = [3, 2, 31, 23, 213, 123, 213, 2]
    is_n_in_array = seq_search(N, array)
    is_n_in_array_sentinel = sentinel_seq_search(N, array)
    print(is_n_in_array)
    print(is_n_in_array_sentinel)

    # return 받는 변수는 하나인데 i, True 로 받아도 오류가 안나고 튜플로 반환받는다
    # 1) return i, True는 실제로는 (i, True) 형태의 튜플 객체를 반환한다.
    # 3) 반환값을 하나의 변수로 받으면 그 튜플 전체를 받게 된다.
    # 2) 파이썬 변수는 자료형을 선언해주지 않기 때문에 모든 자료형을 받을 수 있다.
    # feat GPT. 파이썬에서는 변수의 타입을 정하는 게 아니라, 값(객체)이 자신의 타입을 가진다.

    # 리스트 뿐만 아니라 튜플, 문자열도 인덱싱이 가능한 자료형

    # 추가) 보초법, 탐색 종료조건의 비용을 줄이는 방법 => 리스트 맨 마지막에 보초를 세워서
    #      종료조건을 하나 줄인다(무조건 key를 찾게된다. 그 찾은 index가 마지막이라면 찾지 못했다고 친다.)
    #      파이썬 for문에서는 별로 의미가 없다고 한다. while문에서는 if문이 줄어들으므로 의미가 조금있다.
