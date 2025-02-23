class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse link
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        return prev  # New head of reversed list