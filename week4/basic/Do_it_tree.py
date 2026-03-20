from __future__ import annotations
from typing import Any, Type


class Node:
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key: Any) -> Any:
        # 1. 루트에 주목합니다. 여기서 주목하는 노드를 p라고 합니다
        p = self.root

        # 2. p가 None 이면 검색을 실패하고 종료합니다.
        while True:
            # 3. 검색하는 key와 주목노드 p의 키를 비교합니다.
            if p is None:
                return None

            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:

        # 1. 루트에 주목합니다. 여기서 주목하는 노드를 node라고 한다.
        def add_node(node: Node, key: Any, value: Any) -> None:

            if key == node.key:
                return False
            elif key < node.key:
                # key가 node의 키보다 작으면 왼쪽으로 가야한다.
                # 만약 주목하고 있는 node 의 왼쪽 자식이 없으면 그 자리에 삽입이 가능하다.
                if node.left is None:
                    node.left = Node(key, value, None, None)
                # 만약 왼쪽 자식이 있다면, 한 칸 더 내려간다.
                else:
                    add_node(node.left, key, value)
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)

            return True

        if self.root is None:
            # 셀프 루트가 None, 즉 비어있으면 루트트리를 만들어 줘야한다
            self.root = Node(key, value, None, None)
            return True
        else:
            add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
