# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        :param headA, headB: ListNode
        :rtype: ListNode
        """
        nodes = {}
        a = headA
        while a is not None:
            nodes[a] = 1
            a = a.next

        b = headB
        while b is not None:
            if b in nodes:
                return b.val
            else:
                b = b.next

        return None


if __name__ == '__main__':
    print('Hello World!')
    ball = ListNode(8)

    a = ListNode(4)
    a.next = ListNode(1)
    a.next.next = ball
    ball.next = ListNode(4)
    ball.next.next = ListNode(5)

    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(1)
    b.next.next.next = ball

    s = Solution()
    print(s.getIntersectionNode(a, b))
