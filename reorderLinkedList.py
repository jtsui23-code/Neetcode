from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        # Finds midpoint of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

 
        current = slow
        prev = None
        
        # Reverses the linked list
        while current:

            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

    
        first = head
        second = prev

        while second.next:

            first_next = first.next
            second_next = second.next

            
            first.next = second
            second.next = first_next


            first = first_next
            second = second_next

            if not first:
                break
        



      
        
         
        