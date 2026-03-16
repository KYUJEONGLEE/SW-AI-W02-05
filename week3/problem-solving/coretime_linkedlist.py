# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        i = 1
        j = 1
        l1_result = 0
        l2_result = 0
        while l1 is not None:
            l1_result += l1.val * i
            l1 = l1.next
            i *= 10
        while l2 is not None:
            l2_result += l2.val * j
            l2 = l2.next
            j *= 10

        result = l1_result + l2_result
        result = str(result)
        result = result[::-1]
        result = list(result)

        head = ListNode()
        k = 0
        i = len(result)
        ptr = head
        while i > 0:
            ptr.next = ListNode(int(result[k]))
            ptr = ptr.next
            k += 1
            i -= 1

        return head.next
