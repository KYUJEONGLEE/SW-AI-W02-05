# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def maxDepth(self, root):
        # root를 입력값으로 받는다.
        # 그럼 다음 노드들을 직접 트리로 만들어야?

        # root = TreeNode(3)
        # root.left = TreeNode(9)
        # root.right = TreeNode(20)
        # root.right.left = TreeNode(15)
        # root.right.right = TreeNode(7)

        if root is None:
            return 0

        queue = deque()
        # 큐를 사용해서 루트부터 집어넣고, 트리를 만든다?
        queue.append(root)
        poped_node = []
        while queue:
            p = queue.popleft()
            # 자식 노드가 있는지 확인 할 노드를 pop하고
            if p.left is not None:
                queue.append(p.left)
            elif p.right is not None:
                queue.append(p.right)

            # pop된 노트들의 개수를 세서 깊이를 계산
            poped_node.append(p)

        return
