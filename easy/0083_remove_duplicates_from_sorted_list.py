"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
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
    

class MyList:
    def __init__(self, els:List):
        if len(els) == 0:
            return None
        self.head = ListNode(els[0])
        curr = self.head
        for el in els[1:]:
            tmp = ListNode(el)
            curr.next = tmp
            curr = tmp
    
    def __repr__(self):
        result = ""
        curr = self.head
        while curr:
            result += f" -> {curr.val}"
            curr = curr.next
        return result[4:]
    
    def get_head(self):
        if hasattr(self, 'head'):
            return self.head
        return None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = curr = ListNode(0)
        seen = set()

        while head:
            if head.val in seen:
                head = head.next
            else:
                seen.add(head.val)
                curr.next = ListNode(head.val)
                curr = curr.next
                head = head.next
        return result.next


if __name__ == "__main__":
    inp = MyList([1, 1, 2])
    head = inp.get_head()
    head = Solution().deleteDuplicates(head)    
    assert head.__repr__() == "1 -> 2", head.__repr__()

    inp = MyList([1, 1, 2, 3, 3])
    head = inp.get_head()
    head = Solution().deleteDuplicates(head)
    assert head.__repr__() == "1 -> 2 -> 3", head.__repr__()

    inp = MyList([1, 1, 1])
    head = inp.get_head()
    head = Solution().deleteDuplicates(head)    
    assert head.__repr__() == "1", head.__repr__()
