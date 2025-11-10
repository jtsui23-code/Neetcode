
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        head1 = list1
        head2 = list2
        current = head

        while head1 and head2:
            
            if head1.val >= head2.val:
                temp = head2
                current.next = temp
                head2 = head2.next

            elif head1.val < head2.val:
                temp = head1
                current.next = temp
                head1 = head1.next

            current = current.next

        current.next = head1 if head1 else head2

        return head.next
