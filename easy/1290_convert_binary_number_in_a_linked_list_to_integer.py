"""
Given head which is a reference node to a singly-linked list. The value of each
node in the linked list is either 0 or 1. The linked list holds the binary
representation of a number.
Return the decimal value of the number in the linked list.
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        result = ""
        curr = self
        while curr:
            result += f"{curr.val} -> "
            curr = curr.next
        return result[:-4]

def create_linked_list(arr:List) -> ListNode:
    """
    Returns head of linked list.
    """
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for el in arr[1:]:
        curr.next = ListNode(el)
        curr = curr.next
    return head


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # first pass - get order of the number
        n = -1
        curr = head
        while curr:
            curr = curr.next
            n += 1
        # second pass - compute the result
        result = 0
        curr = head
        while curr:
            if curr.val:
                result += 2 ** n
            n -= 1
            curr = curr.next
        return result


if __name__ == "__main__":
    head = create_linked_list([1, 0, 1])
    out = 5
    actual = Solution().getDecimalValue(head)
    assert actual == out, (actual, out)

    head = create_linked_list([0])
    out = 0
    actual = Solution().getDecimalValue(head)
    assert actual == out, (actual, out)

    head = create_linked_list([1])
    out = 1
    actual = Solution().getDecimalValue(head)
    assert actual == out, (actual, out)

    head = create_linked_list([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])
    out = 18880
    actual = Solution().getDecimalValue(head)
    assert actual == out, (actual, out)

    head = create_linked_list([0, 0])
    out = 0
    actual = Solution().getDecimalValue(head)
    assert actual == out, (actual, out)
