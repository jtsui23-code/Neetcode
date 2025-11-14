from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        before = ListNode(0)
        before.next = head

        slow = before
        fast = before

        for i in range(n+1):
            fast = fast.next
        
        if not fast:
            return before.next.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return before.next
