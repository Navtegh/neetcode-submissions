# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t=0
        curr=head
        while curr:
            curr=curr.next
            t+=1
        curr=head
        prev=None
        for i in range(t-n):
            prev=curr
            curr=curr.next
        if prev:
            prev.next=curr.next
        else:
            head=head.next
        return head
        