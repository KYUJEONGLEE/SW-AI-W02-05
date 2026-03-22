# 문제 링크 : https://www.acmicpc.net/problem/1991

import sys

N = int(sys.stdin.readline())

tree = {}

for node in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = (left, right)


def pre_recursion(node):
    if node == '.':
        return

    print(node, end='')
    pre_recursion(tree[node][0])
    pre_recursion(tree[node][1])


def in_recursion(node):
    if node == '.':
        return

    in_recursion(tree[node][0])
    print(node, end='')
    in_recursion(tree[node][1])


def post_recursion(node):
    if node == '.':
        return

    post_recursion(tree[node][0])
    post_recursion(tree[node][1])
    print(node, end='')


if __name__ == "__main__":
    pre_recursion('A')
    print()
    in_recursion('A')
    print()
    post_recursion('A')
    print()
