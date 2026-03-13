"""
[퀵 정렬 구현]

문제 설명:
- 퀵 정렬(Quick Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 피벗(pivot)을 기준으로 작은 값과 큰 값을 분할하여 재귀적으로 정렬합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [10, 7, 8, 9, 1, 5]
출력: [1, 5, 7, 8, 9, 10]

힌트:
- 피벗 선택 (일반적으로 마지막 원소)
- 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 분할
- 재귀적으로 왼쪽과 오른쪽 부분 정렬
"""

from typing import MutableSequence


def sort3(a: MutableSequence, left: int, right: int, center: int):
    # 피벗 정하는 알고리즘
    # 3개의 값을 정렬하고 가운데 값을 피벗으로 정한다.
    # 가운데 값을 배열 마지막 2번째에 위치 시키면
    # 탐색 할 범위가 유의미하게 줄어든다.

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
    return a


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [10, 7, 8, 9, 1, 5]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = quick_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    # 테스트 케이스 2
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = quick_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()

    # 테스트 케이스 3: 중복 원소
    arr3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("=== 테스트 케이스 3: 중복 원소 ===")
    print(f"정렬 전: {arr3}")
    result3 = quick_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()

    # 테스트 케이스 4: 이미 정렬된 배열
    arr4 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 4: 이미 정렬됨 ===")
    print(f"정렬 전: {arr4}")
    result4 = quick_sort(arr4.copy())
    print(f"정렬 후: {result4}")
    print("이미 정렬된 경우 O(n²) 시간 소요 (최악의 경우)")
