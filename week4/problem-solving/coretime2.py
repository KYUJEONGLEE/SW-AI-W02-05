# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if root is None:
            return []

        answer = []

        q = deque()
        q.append(root)

        while q:
            length_level = len(q)
            level_sum = 0
            for _ in range(length_level):
                cur_q = q.popleft()
                level_sum += cur_q.val

                if cur_q.left is not None:
                    q.append(cur_q.left)
                if cur_q.right is not None:
                    q.append(cur_q.right)

            average = float(level_sum) / length_level
            answer.append(average)

        return answer
