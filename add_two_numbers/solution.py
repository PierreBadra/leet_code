from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = l1
        list1 = []
        while cur:
            list1.insert(0, cur.val)
            cur = cur.next

        cur = l2
        list2 = []
        while cur:
            list2.insert(0, cur.val)
            cur = cur.next

        num1 = int("".join(str(i) for i in list1))
        num2 = int("".join(str(i) for i in list2))

        total = num1 + num2

        dummy = ListNode()
        cur = dummy
        for digit in str(total)[::-1]:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return dummy.next
