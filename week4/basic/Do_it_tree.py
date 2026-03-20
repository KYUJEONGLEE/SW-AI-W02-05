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
        p = self.root
        parent = None
        is_left_child = True

        # 이 반복문에서 key가 bst에 있는지 탐색한다
        # 찾으면 True, 없으면 False를 반환
        # 찾는다면 그 순간의 p의 위치를 가지고 있다.
        while True:
            if p is None:
                return False

            if key == p.key:
                break
            else:
                parent = p
                # 만약 왼쪽 자식이면
                if key < p.key:
                    p = p.left
                    is_left_child = True
                # 오른쪽 자식이면
                else:
                    p = p.right
                    is_left_child = False
        # 찾는다면 p는 삭제할 노드를 참조하고있다.
        # 이제 삭제 할 노드의 자식노드 유무 검사
        if p is self.root:
            self.root = None
            return True
        # 삭제 할 노드가 왼쪽 노드라면
        if is_left_child:
            if p.left is None:
                if p.right is None:
                    # 그 삭제할 노드의 자식이 없다면
                    parent.left = None
                    return True
                else:  # 삭제할 노드에 오른쪽 노드가 있다면
                    parent.right = p.right
                    return True

            elif p.right is None:
                if p.left is None:
                    # 그 삭제할 노드의 자식이 없다면
                    parent.left = None
                    return True
                else:  # 삭제할 노드에 오른쪽 노드가 있다면
                    parent.right = p.right
                    return True
        else:

            # 삭제 할 노드의 자식이 둘 다 없으면 parent 를 None
            # 삭제 할 노드가 root 노드 이면 root 노드 삭제

            # 왼쪽 자식 노드가 있다면,
