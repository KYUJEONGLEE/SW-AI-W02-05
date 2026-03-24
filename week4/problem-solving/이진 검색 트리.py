# 문제 링크 : https://www.acmicpc.net/problem/5639

"""
이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.

노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고,
왼쪽 서브트리, 오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다.
후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다.
예를 들어, 위의 이진 검색 트리의 전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고,
후위 순회 결과는 5 28 24 45 30 60 52 98 50 이다.

이진 검색 트리를 전위 순회한 결과가 주어졌을 때,
이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

전위 순회를 후위 순회로 바꿔라.

전위 : 중 전 후
중위 : 전 중 후
후위 : 전 후 중

전위 순회로 입력받은 값들을 트리 형태로 만든다..?
트리로 만들지 않고, 하는 방법이 없을까

전위 순회로 들어온다고 했으므로 루트 노드는 맨 앞 숫자.
전위 순회를 내려가다가 가장 작은 숫자가 나오면 그 숫자가 가장 왼쪽에 있는 노드 => o

"""
import sys
sys.setrecursionlimit(10 ** 6)
V = []


while True:
    v = sys.stdin.readline()

    if v == '':
        break

    V.append(int(v))


def recursion(start, end):
    if start > end:
        return

    root = V[start]

    split = end + 1

    for node in range(start + 1, end + 1):
        if V[node] > root:
            split = node
            break

    recursion(start + 1, split - 1)
    recursion(split, end)
    print(root)


recursion(0, len(V) - 1)
