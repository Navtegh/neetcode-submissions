# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        curr2=head
        while curr2 and curr2.next:
            curr=curr.next
            curr2=curr2.next.next
            if curr==curr2:
                return True
        return False
