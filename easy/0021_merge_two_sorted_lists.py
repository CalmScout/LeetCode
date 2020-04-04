"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        result = [self.val]
        pointer = self
        while pointer.next:
            pointer = pointer.next
            result.append(pointer.val)
        return str(result)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(42)
        l3 = result
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
        tail = l1 if l2 is None else l2
        l3.next = tail
        return result.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    out = str([1, 1, 2, 3, 4, 4])
    actual = Solution().mergeTwoLists(l1, l2).__repr__()
    assert out == actual, (out, actual)

    l1 = ListNode(-9)
    l1.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(7)

    out = str([-9, 3, 5, 7])
    actual = Solution().mergeTwoLists(l1, l2).__repr__()
    assert out == actual, (out, actual)
