"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""
from typing import List


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
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


if __name__ == "__main__":
    def create(arr:List[int]) -> ListNode:
        result = ListNode(arr[0])
        p = result
        for val in arr[1:]:
            p.next = ListNode(val)
            p = p.next
        return result
    
    inp = create([1, 2, 3, 4, 5])
    out = create([3, 4, 5]).__repr__()
    actual = Solution().middleNode(inp).__repr__()
    assert actual == out, (actual, out)

    inp = create([1, 2, 3, 4, 5, 6])
    out = create([4, 5, 6]).__repr__()
    actual = Solution().middleNode(inp).__repr__()
    assert actual == out, (actual, out)

    inp = create([1, 2])
    out = create([2]).__repr__()
    actual = Solution().middleNode(inp).__repr__()
    assert actual == out, (actual, out)

    inp = create([1, 2, 3, 4])
    out = create([3, 4]).__repr__()
    actual = Solution().middleNode(inp).__repr__()
    assert actual == out, (actual, out)
