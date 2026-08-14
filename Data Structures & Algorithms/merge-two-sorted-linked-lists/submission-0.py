# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        curr1=list1
        curr2=list2
        head=ListNode()
        curr3=head
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val<curr2.val:
                    curr3.next=curr1
                    curr3=curr3.next
                    curr1=curr1.next
                else:
                    curr3.next=curr2
                    curr3=curr3.next
                    curr2=curr2.next
            elif curr1:
                while curr1:
                    curr3.next=curr1
                    curr3=curr3.next
                    curr1=curr1.next
            elif curr2:
                while curr2:
                    curr3.next=curr2
                    curr3=curr3.next
                    curr2=curr2.next

        return head.next


