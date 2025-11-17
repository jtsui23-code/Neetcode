from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        hash_map = {}

        current = head
        while current:
            hash_map[current] = Node(current.val)
            current = current.next

        # Reset to travrse again
        current = head

        while current:
            
            if current.next:
                hash_map[current].next = hash_map[current.next]
            else: 
                hash_map[current].next = None


            if current.random:
                hash_map[current].random = hash_map[current.random]
            else:
                hash_map[current].random = None


            current = current.next

        return hash_map[head]
        