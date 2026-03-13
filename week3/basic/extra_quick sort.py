from typing import MutableSequence


def sort3(a: MutableSequence, left: int, right: int, center: int):
    # 피벗 정하는 알고리즘
    if a[center] < a[left]:
        a[left], a[center] = a[center], a[left]
    if a[right] < a[center]:
        a[right], a[center] = a[center], a[right]
    if a[center] < a[left]:
        a[left], a[center] = a[center], a[left]

    return center


def q_sort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    pc = (left + right) // 2

    pivot_index = sort3(a, pl, pr, pc)
    pivot = a[pivot_index]

    a[pr - 1], a[pivot_index] = a[pivot_index], a[pr - 1]
    # 피벗의 위치를 마지막 2번쨰 위치로 바꿈
    pl += 1
    pr -= 2

    while pl <= pr:
        while a[pl] < pivot:
            pl += 1
        while a[pr] > pivot:
            pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    # 아래와 같은 조건문을 붙이는 이유는
    # 한쪽 구간의 크기가 0개 or 1개일 수 있기 때문에
    # 이미 정렬된 구간은 재귀호출 할 필요가 없다.
    if left < pr:
        # 왼쪽 구간에 원소가 2개 이상 있는지확인
        # 왼쪽 구간은 left ~ pr 까지 나뉘고
        # 오른쪽 구간은 pl ~ right 으로 나뉜다.
        # left < pr 일때만 원소가 2개 이상
        q_sort(a, left, pr)
    if pl < right:
        q_sort(a, pl, right)


def quick_sort(a: MutableSequence) -> None:
    q_sort(a, 0, len(a) - 1)


if __name__ == "__main__":
    X = [3, 8, 2, 1, 9, 6, 7, 4, 13, 11, 5, 12, 10]
    print(X)
    quick_sort(X)
    print(X)
