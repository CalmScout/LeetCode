"""
You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order and each of their nodes contain a single digit. Add the two numbers and
return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        result = []
        p = self
        while p:
            result.append(p.val)
            p = p.next
        return str(result)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        result = ListNode((l1.val + l2.val) % 10)
        l3 = result
        overflow = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            s = l1.val + l2.val + overflow
            l3.next = ListNode(s % 10)
            overflow = s // 10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        tail = l1 if not l1 is None else l2
        while tail:
            s = tail.val + overflow
            l3.next = ListNode(s % 10)
            overflow = s // 10
            l3 = l3.next
            tail = tail.next
        if overflow == 1:
            l3.next = ListNode(1)
        return result


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    l3 = ListNode(7)
    l3.next = ListNode(0)
    l3.next.next = ListNode(8)
    
    out = l3.__repr__()
    actual = Solution().addTwoNumbers(l1, l2).__repr__()
    
    assert actual == out, (actual, out)
